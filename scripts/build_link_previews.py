#!/usr/bin/env python3
"""Build hover cards for links in public blog posts. Never reads notes or draft storage."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import re
import time
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit

from bs4 import BeautifulSoup
from link_metadata import Resource, fetch_public, page_metadata, thumbnail

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://thomas.jiralerspong.com'


def key(url):
    parts = urlsplit(url)
    path = re.sub(r'index\.html$', '', parts.path or '/')
    if parts.hostname in {'thomas.jiralerspong.com', 'superkaiba.github.io'}:
        return urlunsplit(('https', 'thomas.jiralerspong.com', path, parts.query, parts.fragment))
    return urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.fragment))


def snippet(node, limit=400):
    return ' '.join(node.get_text(' ', strip=True).split())[:limit] if node else ''


def local_image(node, base):
    image = node.find('img', src=True) if node else None
    if image:
        url = urlsplit(urljoin(base, image['src']))
        if url.hostname == urlsplit(ORIGIN).hostname and url.path.startswith('/assets/'):
            return url.path
    return None


def document_metadata(soup, url, target=None):
    if target:
        if target.name not in {'section', 'article', 'li', 'div', 'details'} and not re.match('h[1-6]', target.name):
            target = target.find_parent(['article', 'section', 'li']) or target
        heading = target if re.match('h[1-6]', target.name) else target.find(['h1', 'h2', 'h3', 'h4', 'h5', 'summary'])
        paragraph = target.select_one('.project-reading p, .paper-description, .paper-summary, .blog-deck') or target.find('p') or target.find('li')
        if re.match('h[1-6]', target.name):
            paragraph = target.find_next_sibling('p')
        return {'title': snippet(heading, 200) or snippet(target, 160), 'description': snippet(paragraph),
                'image': local_image(target, url), 'site': 'Thomas Jiralerspong', 'available': True, 'internal': True}
    metadata = page_metadata(Resource(url, 'text/html', str(soup).encode()))
    main = soup.find('main') or soup.body
    if not metadata['description']:
        metadata['description'] = snippet(main.find('p') if main else None)
    image = metadata.pop('image_url')
    image = urlsplit(image).path if image and urlsplit(image).hostname == urlsplit(ORIGIN).hostname else local_image(main, url)
    if image and not image.startswith('/assets/'):
        image = None
    return {**metadata, 'image': image, 'site': 'Thomas Jiralerspong', 'available': True, 'internal': True}


def collect(site):
    links, documents, internal = {}, {}, {}
    # Explicit public page roots exclude LaTeX sources, markdown proposals marked unpublished,
    # repository metadata, and any private/local working directories.
    pages = sorted(site.glob('*.html')) + sorted((site / 'blog').rglob('*.html')) + [site / 'projects/index.html']
    for path in pages:
        if not path.is_file():
            continue
        soup = BeautifulSoup(path.read_text(), 'html.parser')
        if soup.find('meta', attrs={'http-equiv': re.compile('refresh', re.I)}):
            continue
        robots = soup.find('meta', attrs={'name': 'robots'})
        if robots and 'noindex' in robots.get('content', '').lower():
            continue
        url = key(ORIGIN + '/' + path.relative_to(site).as_posix())
        documents[url] = soup
        for anchor in soup.select('article.blog-body a[href]:not([data-no-preview])'):
            destination = key(urljoin(url, anchor['href']))
            parts = urlsplit(destination)
            if parts.scheme not in {'http', 'https'} or parts.username or parts.password:
                continue
            label = snippet(anchor, 200) or anchor.get('aria-label') or parts.hostname
            context = anchor.find_parent('article', class_='paper')
            fallback = {'title': label, 'description': '', 'site': parts.hostname, 'image': None, 'available': False}
            if context and label.lower() in {'paper', 'pdf', 'arxiv'}:
                fallback.update(title=snippet(context.find(['h2', 'h3']), 200) or label,
                                description=snippet(context.select_one('.paper-description, .paper-summary')),
                                image=local_image(context, url), available=True)
            if destination not in links or len(fallback['title']) > len(links[destination]['title']):
                links[destination] = fallback
    for url, fallback in links.items():
        base, _, fragment = url.partition('#')
        if base in documents:
            target = documents[base].find(id=unquote(fragment)) if fragment else None
            internal[url] = document_metadata(documents[base], base, target)
        elif urlsplit(url).hostname == urlsplit(ORIGIN).hostname:
            internal[url] = {**fallback, 'site': 'Thomas Jiralerspong', 'internal': True}
    return links, internal


def external_preview(url, fallback, destination):
    try:
        deadline = time.monotonic() + 10
        resource = fetch_public(url, limit=1_000_000, accept='text/html,application/xhtml+xml', deadline=deadline)
        metadata = page_metadata(resource)
        if re.search(r'^(just a moment|attention required|access denied|robot or human|security check)', metadata['title'], re.I):
            return fallback
        image_url = metadata.pop('image_url')
        result = {**fallback, **{k: v for k, v in metadata.items() if v},
                  'available': bool(metadata['title'] or metadata['description'] or fallback['available'])}
        if image_url:
            try:
                resource = fetch_public(image_url, limit=4_000_000, accept='image/jpeg,image/png,image/webp,image/gif', deadline=deadline)
                image = thumbnail(resource)
                name = hashlib.sha256(image).hexdigest()[:24] + '.jpg'
                (destination / name).write_bytes(image)
                result.update(image='/assets/link-previews/' + name, available=True)
            except Exception:
                pass
        return result
    except Exception:
        return fallback


def build(site=ROOT, *, refresh=False, offline=False):
    destination = site / 'assets/link-previews'
    destination.mkdir(parents=True, exist_ok=True)
    index = destination / 'index.json'
    previous = json.loads(index.read_text()).get('links', {}) if index.exists() else {}
    links, result = collect(site)
    external = {}
    for url, fallback in links.items():
        if url in result:
            continue
        base = url.split('#')[0]
        if base not in external or len(fallback['title']) > len(external[base]['title']):
            external[base] = fallback
    pending = {}
    for url, fallback in external.items():
        if not refresh and url in previous:
            result[url] = previous[url]
        elif offline:
            result[url] = fallback
        else:
            pending[url] = fallback
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(external_preview, url, fallback, destination): url for url, fallback in pending.items()}
        for count, future in enumerate(as_completed(futures), 1):
            result[futures[future]] = future.result()
            if count % 25 == 0 or count == len(futures):
                print(f'Prepared {count}/{len(futures)} external link previews', flush=True)
    for url in links:
        if url not in result and url.split('#')[0] in result:
            result[url] = result[url.split('#')[0]]
    used_images = {item.get('image') for item in result.values()}
    for image in destination.glob('*.jpg'):
        if '/assets/link-previews/' + image.name not in used_images:
            image.unlink()
    index.write_text(json.dumps({'links': result}, ensure_ascii=False, separators=(',', ':'), sort_keys=True) + '\n')
    print(f'Wrote {len(result)} preview destinations, {sum(bool(v["image"]) for v in result.values())} with images.', flush=True)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true', help='Refresh previously cached external pages')
    parser.add_argument('--offline', action='store_true', help='Update internal previews without fetching external pages')
    args = parser.parse_args()
    build(refresh=args.refresh, offline=args.offline)

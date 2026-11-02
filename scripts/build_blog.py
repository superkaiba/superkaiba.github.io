"""Refresh newsletter previews from public RSS without copying article bodies."""
import argparse
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from hashlib import sha256
from html import escape, unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = "https://thomasjiralerspong.substack.com"
CUSTOM = "https://blog.thomas.jiralerspong.com"
ALLOWED_HOSTS = {urlsplit(ORIGINAL).hostname, urlsplit(CUSTOM).hostname}
CACHE = ROOT / ".cache/substack/previews.json"
MARKER = r"<!-- LATEST POSTS START -->.*?<!-- LATEST POSTS END -->"


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def plain(value):
    parser = PlainText()
    parser.feed(value)
    return " ".join(unescape(" ".join(parser.parts)).split())


def post_path(url):
    parsed = urlsplit(url)
    if (parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS
            or parsed.username or parsed.password or parsed.port
            or not re.fullmatch(r"/p/[a-zA-Z0-9_-]+", parsed.path)):
        raise ValueError("Unexpected post URL in publication feed")
    return parsed.path


def parse_feed(data):
    root = ET.fromstring(data)
    posts = {}
    for item in root.findall("./channel/item"):
        path = post_path(item.findtext("link", ""))
        title = plain(item.findtext("title", ""))
        if not title:
            raise ValueError("Post has no title")
        published = parsedate_to_datetime(item.findtext("pubDate", ""))
        if published.tzinfo is None:
            published = published.replace(tzinfo=timezone.utc)
        image = ""
        enclosure = item.find("enclosure")
        if enclosure is not None and enclosure.get("type", "").startswith("image/"):
            candidate = enclosure.get("url", "")
            parsed = urlsplit(candidate)
            if parsed.scheme == "https" and parsed.hostname in {
                "substack-post-media.s3.amazonaws.com", "substackcdn.com"
            }:
                image = candidate
        posts[path] = dict(path=path, title=title,
                           description=plain(item.findtext("description", ""))[:500],
                           published=published.astimezone(timezone.utc).isoformat(), image=image)
    if not posts:
        raise ValueError("Publication feed contains no posts")
    return sorted(posts.values(), key=lambda p: p["published"], reverse=True)[:10]


def refresh(config, offline=False):
    fallback = config["recent_posts"]
    if CACHE.is_file():
        try:
            cached = json.loads(CACHE.read_text())
            if cached:
                for p in cached:
                    post_path(ORIGINAL + p["path"])
                    datetime.fromisoformat(p["published"])
                fallback = cached
        except (ValueError, KeyError, TypeError):
            pass
    if offline:
        return fallback
    try:
        request = Request(config["publication_url"] + "/feed", headers={
            "User-Agent": "ThomasWebsiteFeed/1.0 (+https://thomas.jiralerspong.com/)",
            "Accept": "application/rss+xml, application/xml",
        })
        with urlopen(request, timeout=25) as response:
            if urlsplit(response.url).hostname not in ALLOWED_HOSTS:
                raise ValueError("Feed redirected outside the publication")
            data = response.read(8_000_001)
        if len(data) > 8_000_000:
            raise ValueError("Feed exceeds size limit")
        posts = parse_feed(data)
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        CACHE.write_text(json.dumps(posts, ensure_ascii=False, indent=2) + "\n")
        print(f"Loaded {len(posts)} public newsletter previews")
        return posts
    except (OSError, ValueError, ET.ParseError) as error:
        print(f"::warning::Newsletter feed unavailable ({type(error).__name__}). Keeping saved previews.")
        return fallback


def render_latest(publication, posts):
    cards = []
    for post in posts[:2]:
        url = escape(publication + post["path"], quote=True)
        title = escape(post["title"])
        date = datetime.fromisoformat(post["published"])
        pretty = date.strftime("%B %d, %Y").replace(" 0", " ")
        cover = ""
        if post.get("image"):
            cover = (f'<a class="blog-card-cover" href="{url}" aria-label="Read {title}">'
                     f'<img class="blog-card-image" src="{escape(post["image"], quote=True)}" '
                     'alt="" loading="lazy" decoding="async"></a>')
        item_class = '' if cover else ' class="no-cover"'
        cards.append(f'<li{item_class}>{cover}<div>'
                     f'<h3><a href="{url}">{title}</a></h3>'
                     f'<p class="latest-subtitle">{escape(post["description"])}</p>'
                     f'<p class="latest-meta"><time datetime="{date.date()}">{pretty}</time></p>'
                     '</div></li>')
    return ('<!-- LATEST POSTS START --><aside class="latest-posts" aria-labelledby="latest-posts-heading">'
            '<div class="latest-posts-heading"><h2 id="latest-posts-heading">Latest posts</h2>'
            f'<a href="{publication}/archive">All posts →</a></div>'
            '<p class="blog-cadence">Essays on research, AI, and life.</p>'
            f'<p class="newsletter-action"><a class="newsletter-button" href="{publication}/subscribe">'
            'Get new essays by email</a></p><ol>' + ''.join(cards) + '</ol></aside><!-- LATEST POSTS END -->')


def update_pages(root, config, posts):
    publication = config["publication_url"].rstrip("/")
    if publication not in {ORIGINAL, CUSTOM}:
        raise ValueError("Unknown publication")
    home = root / "index.html"
    text, count = re.subn(MARKER, lambda _: render_latest(publication, posts), home.read_text(), flags=re.S)
    if count != 1:
        raise ValueError("Expected one Latest posts region")
    home.write_text(text)
    css_version = sha256((root / "css/blog.css").read_bytes()).hexdigest()[:10]
    for page in [*root.glob("*.html"), *root.glob("blog/**/index.html")]:
        text = page.read_text()
        # Keep existing published article text and archive entries intact.
        for old in (ORIGINAL, CUSTOM):
            text = text.replace(f'href="{old}/subscribe"', f'href="{publication}/subscribe"')
            text = text.replace(f'href="{old}"><span>Substack</span>',
                                f'href="{publication}"><span>Blog</span>')
            text = text.replace(f'href="{old}"><span>Blog</span>',
                                f'href="{publication}"><span>Blog</span>')
        if page == root / "blog/index.html":
            text = text.replace('<title>Blog —', '<title>Blog archive —')
            header = ('<header class="blog-header"><p class="blog-kicker">Thomas Jiralerspong</p>'
                      '<h1>Blog archive</h1><p class="blog-deck">Earlier essays on research, AI, and life.</p>'
                      '<div class="newsletter-notice"><p>New essays are published on my blog.</p>'
                      f'<p><a class="newsletter-button" href="{publication}">Read the blog</a> '
                      f'<a href="{publication}/subscribe">Subscribe by email</a></p></div>'
                      '<p class="blog-meta"><a href="/blog/feed.xml">Archive RSS</a></p></header>')
            text = re.sub(r'<header class="blog-header">.*?</header>', lambda _: header, text, count=1, flags=re.S)
        elif page.parent.parent.name == "blog" and '<article class="blog-body">' in text:
            notice = ('<!-- NEWSLETTER NOTICE START --><aside class="newsletter-notice" aria-label="Newsletter">'
                      '<p>Get new essays on research, AI, and life.</p>'
                      f'<p><a class="newsletter-button" href="{publication}/subscribe">Subscribe by email</a> '
                      f'<a href="{publication}">Read the current blog →</a></p></aside><!-- NEWSLETTER NOTICE END -->')
            text = re.sub(r'<!-- NEWSLETTER NOTICE START -->.*?<!-- NEWSLETTER NOTICE END -->', '', text, flags=re.S)
            text = text.replace('<article class="blog-body">', notice + '<article class="blog-body">', 1)
            text = text.replace('>All posts</a>', '>Earlier essays</a>')
        text = re.sub(r'(href="/?css/blog\.css)\?[^"\s]+', lambda m: m[1] + '?v=' + css_version, text)
        page.write_text(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="Use saved previews")
    args = parser.parse_args()
    config = json.loads((ROOT / "data/blog-publication.json").read_text())
    update_pages(ROOT, config, refresh(config, args.offline))


if __name__ == "__main__":
    main()

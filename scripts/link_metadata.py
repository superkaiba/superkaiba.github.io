"""Fetch bounded metadata and thumbnails from public web pages for the static build."""
from dataclasses import dataclass
import http.client
import io
import ipaddress
import socket
import ssl
import time
from urllib.parse import urljoin, urlsplit, urlunsplit

from bs4 import BeautifulSoup
from PIL import Image


class PreviewUnavailable(ValueError):
    pass


def public_url(value):
    if not isinstance(value, str) or len(value) > 4096 or any(ord(c) < 32 for c in value):
        raise PreviewUnavailable()
    try:
        parts = urlsplit(value)
        if parts.scheme not in {'http', 'https'} or not parts.hostname or parts.username is not None or parts.password is not None:
            raise PreviewUnavailable()
        host = parts.hostname.encode('idna').decode('ascii').lower().rstrip('.')
        port = parts.port or (443 if parts.scheme == 'https' else 80)
        if port not in {80, 443} or host == 'localhost' or host.endswith(('.localhost', '.local', '.internal', '.ts.net')):
            raise PreviewUnavailable()
        authority = f'[{host}]' if ':' in host else host
        if parts.port:
            authority += ':' + str(port)
        return urlunsplit((parts.scheme, authority, parts.path or '/', parts.query, ''))
    except (ValueError, UnicodeError):
        raise PreviewUnavailable() from None


def public_address(host, port):
    addresses = list(dict.fromkeys(info[4][0] for info in socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)))
    if not addresses:
        raise PreviewUnavailable()
    # Check every answer, then connect to that exact address to prevent DNS rebinding.
    for address in addresses:
        ip = ipaddress.ip_address(address)
        if not ip.is_global or ip.is_multicast or getattr(ip, 'ipv4_mapped', None) or getattr(ip, 'sixtofour', None) or getattr(ip, 'teredo', None):
            raise PreviewUnavailable()
    return addresses[0]


@dataclass
class Resource:
    url: str
    content_type: str
    body: bytes


def fetch_public(url, *, limit, accept, deadline):
    for _ in range(4):
        url = public_url(url)
        parts = urlsplit(url)
        port = parts.port or (443 if parts.scheme == 'https' else 80)
        address = public_address(parts.hostname, port)
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise PreviewUnavailable()
        timeout = min(3, remaining)
        connection = http.client.HTTPConnection(parts.hostname, port, timeout=timeout)
        response = None
        try:
            sock = socket.create_connection((address, port), timeout=timeout)
            if parts.scheme == 'https':
                try:
                    sock = ssl.create_default_context().wrap_socket(sock, server_hostname=parts.hostname)
                except Exception:
                    sock.close()
                    raise
            connection.sock = sock
            path = urlunsplit(('', '', parts.path or '/', parts.query, ''))
            connection.request('GET', path, headers={'User-Agent': 'ThomasWebsite-LinkPreview/1.0',
                               'Accept': accept, 'Accept-Encoding': 'identity', 'Connection': 'close'})
            response = connection.getresponse()
            if response.status in {301, 302, 303, 307, 308}:
                destination = response.getheader('Location')
                if not destination:
                    raise PreviewUnavailable()
                url = urljoin(url, destination)
                continue
            if response.status != 200 or response.getheader('Content-Encoding', 'identity').lower() != 'identity':
                raise PreviewUnavailable()
            chunks, size = [], 0
            while size <= limit:
                if response.isclosed():
                    break
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise PreviewUnavailable()
                sock.settimeout(min(3, remaining))
                chunk = response.read1(min(65536, limit + 1 - size))
                if not chunk:
                    break
                chunks.append(chunk)
                size += len(chunk)
            if size > limit:
                raise PreviewUnavailable()
            return Resource(url, response.getheader('Content-Type', '').split(';')[0].lower(), b''.join(chunks))
        finally:
            if response is not None:
                response.close()
            connection.close()
    raise PreviewUnavailable()


def page_metadata(resource):
    if resource.content_type not in {'text/html', 'application/xhtml+xml'}:
        raise PreviewUnavailable()
    soup = BeautifulSoup(resource.body, 'html.parser')
    def clean(value, limit):
        return ' '.join(BeautifulSoup(value or '', 'html.parser').get_text(' ', strip=True).split())[:limit]
    def meta(*names):
        for name in names:
            tag = soup.find('meta', attrs={'property': name}) or soup.find('meta', attrs={'name': name})
            if tag and tag.get('content'):
                return tag['content']
        return ''
    title = clean(meta('og:title', 'twitter:title') or (soup.title.get_text() if soup.title else ''), 220)
    description = clean(meta('og:description', 'twitter:description', 'description'), 440)
    if not description:
        paragraph = soup.select_one('main p, article p')
        if paragraph:
            description = clean(paragraph.get_text(' ', strip=True), 440)
    site = clean(meta('og:site_name'), 100) or urlsplit(resource.url).hostname
    image = meta('og:image:secure_url', 'og:image', 'twitter:image', 'twitter:image:src')
    return {'title': title, 'description': description, 'site': site,
            'image_url': urljoin(resource.url, image) if image else None}


def thumbnail(resource):
    if resource.content_type not in {'image/jpeg', 'image/png', 'image/webp', 'image/gif'}:
        raise PreviewUnavailable()
    with Image.open(io.BytesIO(resource.body)) as image:
        if image.width * image.height > 16_000_000 or image.format not in {'JPEG', 'PNG', 'WEBP', 'GIF'}:
            raise PreviewUnavailable()
        image.thumbnail((960, 540))
        rgba = image.convert('RGBA')
        flattened = Image.new('RGB', image.size, 'white')
        flattened.paste(rgba, mask=rgba.getchannel('A'))
        output = io.BytesIO()
        flattened.save(output, format='JPEG', quality=82)
        return output.getvalue()

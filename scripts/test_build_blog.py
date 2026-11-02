"""Checks for publication-feed ingestion and preserving the existing archive."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import URLError

import build_blog as blog


def item(slug="first", date="Tue, 27 Oct 2026 22:16:45 GMT", title="An essay"):
    return (f"<item><title>{title}</title><link>{blog.ORIGINAL}/p/{slug}</link>"
            f"<pubDate>{date}</pubDate><description>&lt;b&gt;A &amp;amp; B&lt;/b&gt;</description>"
            "<enclosure type='image/jpeg' url='https://substack-post-media.s3.amazonaws.com/public/cover.png'/>"
            "</item>")


def feed(*items):
    return ("<rss><channel>" + "".join(items) + "</channel></rss>").encode()


class BlogTests(unittest.TestCase):
    def test_feed_order_entities_and_rendering(self):
        posts = blog.parse_feed(feed(item("old", "Mon, 26 Oct 2026 12:00:00 GMT"), item("new")))
        self.assertEqual([p["path"] for p in posts], ["/p/new", "/p/old"])
        self.assertEqual(posts[0]["description"], "A & B")
        posts[0]["title"] = '<img src=x onerror="bad()">'
        rendered = blog.render_latest(blog.CUSTOM, posts)
        self.assertIn(blog.CUSTOM + "/p/new", rendered)
        self.assertNotIn('<img src=x', rendered)
        self.assertIn('A &amp; B', rendered)

    def test_reject_wrong_publication_and_empty_feed(self):
        with self.assertRaises(ValueError):
            blog.parse_feed(feed(item()).replace(blog.ORIGINAL.encode(), b'https://example.com'))
        with self.assertRaises(ValueError):
            blog.parse_feed(feed())
        with self.assertRaises(ValueError):
            blog.post_path(blog.ORIGINAL + '/publish/post/123')

    def test_feed_outage_keeps_most_recent_cached_previews(self):
        posts = blog.parse_feed(feed(item("cached")))
        config = {"publication_url":blog.ORIGINAL, "recent_posts":blog.parse_feed(feed(item("older")))}
        with tempfile.TemporaryDirectory() as directory:
            cache = Path(directory) / "previews.json"
            cache.write_text(json.dumps(posts))
            with patch.object(blog, 'CACHE', cache), patch.object(blog, 'urlopen', side_effect=URLError('unavailable')):
                self.assertEqual(blog.refresh(config), posts)

    def test_archive_body_and_original_rss_are_preserved(self):
        posts = blog.parse_feed(feed(item()))
        config = {"publication_url":blog.CUSTOM, "recent_posts":posts}
        body = '<article class="blog-body"><h2>Original essay</h2><p>Keep every word &amp; link.</p></article>'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'css').mkdir(); (root/'css/blog.css').write_text('body{}')
            (root/'blog/old').mkdir(parents=True)
            (root/'index.html').write_text('<!-- LATEST POSTS START -->old<!-- LATEST POSTS END -->')
            (root/'blog/index.html').write_text('<title>Blog — Thomas</title><header class="blog-header">Old</header><ol>Archive entries</ol>')
            (root/'blog/old/index.html').write_text('<header class="blog-header">Title</header>'+body)
            (root/'blog/feed.xml').write_text('existing archive feed')
            blog.update_pages(root, config, posts)
            first = (root/'blog/old/index.html').read_text()
            self.assertIn(body, first)
            self.assertIn('Blog archive', (root/'blog/index.html').read_text())
            self.assertIn('Archive entries', (root/'blog/index.html').read_text())
            self.assertEqual((root/'blog/feed.xml').read_text(), 'existing archive feed')
            blog.update_pages(root, config, posts)
            self.assertEqual((root/'blog/old/index.html').read_text(), first)


if __name__ == '__main__':
    unittest.main()

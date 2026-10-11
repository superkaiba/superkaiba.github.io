import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import markdown
import build_projects

from build_projects import render_markdown


class ProjectMathTests(unittest.TestCase):
    def test_math_is_opt_in(self):
        body = "Costs $5 and $10. Keep $z_t$ literal.\n\n- Existing list"
        self.assertEqual(render_markdown(body), markdown.markdown(body, extensions=["sane_lists"]))

    def test_inline_math_preserves_subscripts_and_prefix_comparison(self):
        html = render_markdown(r"Infer $q_t(z \mid x_{<t})$ from a prefix.", True)
        root = ET.fromstring(html)
        ns = {"m": "http://www.w3.org/1998/Math/MathML"}
        self.assertEqual(len(root.findall(".//m:msub", ns)), 2)
        self.assertIn("<", "".join(root.itertext()))
        self.assertNotIn("<script", html)

    def test_display_math_is_scrollable_and_native(self):
        html = render_markdown(r"$$p(x) = \int p(x \mid z)q(z)\,dz$$", True)
        root = ET.fromstring(html)
        equation = root.find("span")
        self.assertEqual(equation.attrib["class"], "project-equation")
        math = equation.find("{http://www.w3.org/1998/Math/MathML}math")
        self.assertEqual(math.attrib["display"], "block")
        self.assertNotIn("math/tex", html)

    def test_code_and_escaped_dollars_stay_literal(self):
        html = render_markdown(r"`$z_t$` and \$5", True)
        self.assertIn("<code>$z_t$</code>", html)
        self.assertIn("$5", html)
        self.assertNotIn("<math", html)


class ProjectPageTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.content = self.root / "content/projects"
        self.dest = self.root / "projects"
        self.content.mkdir(parents=True)
        for name in ("css/style.css", "js/script.js"):
            path = self.root / name
            path.parent.mkdir(exist_ok=True)
            path.write_text("")
        (self.content / "alpha.md").write_text('''---
title: Alpha & one
status: In progress
order: 1
math: true
aliases:
- old-alpha
---
# Alpha & one

Alpha's distinctive content with $z_t$.

[Related](#beta) [Alias](#old-beta) [Local](#details)
[External](https://example.com/#beta) [Document](/assets/docs/example.pdf)
''')
        (self.content / "beta.md").write_text('''---
title: Beta
status: Not started
order: 2
aliases:
- old-beta
---
# Beta

Beta's distinctive content.
''')
        (self.content / "hidden.md").write_text('''---
title: Hidden proposal
status: Not started
order: 3
published: false
aliases:
- old-hidden
---
# Hidden proposal

Unpublished content.
''')
        for slug in ("hidden", "old-hidden"):
            (self.dest / slug).mkdir(parents=True)
            for name in ("index.html", "note.md"):
                (self.dest / slug / name).write_text("Previously published")
        with patch.multiple(build_projects, ROOT=self.root, CONTENT=self.content, DEST=self.dest):
            build_projects.main()

    def test_standalone_page_contains_one_project_with_working_assets_and_links(self):
        html = (self.dest / "alpha/index.html").read_text()
        self.assertIn("<h1>Alpha &amp; one</h1>", html)
        self.assertIn("<title>Alpha &amp; one · Thomas Jiralerspong</title>", html)
        self.assertIn('rel="canonical" href="https://thomas.jiralerspong.com/projects/alpha/"', html)
        self.assertIn("Alpha's distinctive content", html)
        self.assertNotIn("Beta's distinctive content", html)
        self.assertNotIn('http-equiv="refresh"', html)
        for asset in ("base.css", "catalogue.css", "navigation.js"):
            self.assertIn(f'../{asset}?v=', html)
            self.assertTrue((self.dest / asset).exists())
        self.assertIn('href="../">← All projects', html)
        self.assertIn('href="../#alpha">View in catalogue', html)
        self.assertIn('href="../beta/">Related', html)
        self.assertIn('href="../beta/">Alias', html)
        self.assertIn('href="#details">Local', html)
        self.assertIn('href="https://example.com/#beta">External', html)
        self.assertIn('href="/assets/docs/example.pdf">Document', html)
        self.assertIn("<math", html)

    def test_catalogue_keeps_hash_links_and_aliases_open_standalone_pages(self):
        catalogue = (self.dest / "index.html").read_text()
        self.assertIn("Alpha's distinctive content", catalogue)
        self.assertIn("Beta's distinctive content", catalogue)
        self.assertIn('id="alpha"', catalogue)
        self.assertIn('id="old-alpha"', catalogue)
        self.assertIn('href="#alpha" data-section="alpha"', catalogue)
        self.assertIn('<h3><a href="alpha/">Alpha &amp; one</a></h3>', catalogue)
        alias = (self.dest / "old-alpha/index.html").read_text()
        self.assertIn('http-equiv="refresh" content="0;url=../alpha/"', alias)
        self.assertIn('rel="canonical" href="https://thomas.jiralerspong.com/projects/alpha/"', alias)
        self.assertEqual((self.dest / "old-alpha/note.md").read_text(), (self.dest / "alpha/note.md").read_text())

    def test_unpublished_projects_and_aliases_are_removed(self):
        catalogue = (self.dest / "index.html").read_text()
        self.assertNotIn("Hidden proposal", catalogue)
        self.assertNotIn("Unpublished content", catalogue)
        for slug in ("hidden", "old-hidden"):
            for name in ("index.html", "note.md"):
                self.assertFalse((self.dest / slug / name).exists())


if __name__ == "__main__":
    unittest.main()

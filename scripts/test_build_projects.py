import unittest
import xml.etree.ElementTree as ET

import markdown

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


if __name__ == "__main__":
    unittest.main()

import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, Boot.dev!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(node.props_to_html(), ' class="greeting" href="https://boot.dev"',)

    def test_values(self):
        node = HTMLNode(
            "div",
            "The cake is a lie",
        )
        self.assertEqual(node.tag,"div",)
        self.assertEqual(node.value,"The cake is a lie",)
        self.assertEqual(node.children,None,)
        self.assertEqual(node.props,None,)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange project",
            None,
            {"class": "primary"},
        )
        self.assertEqual(node.__repr__(),"HTMLNode(p, What a strange project, children: None, {'class': 'primary'})",)


if __name__ == "__main__":
    unittest.main()

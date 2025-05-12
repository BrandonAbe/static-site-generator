import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Random Text!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Random Text!</a>',)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild node")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild node</b></span></div>",)

    def test_to_html_multiple_children(self):
        node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",)

    def test_headings(self):
        node = ParentNode("h2",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)
        self.assertEqual(node.to_html(),"<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",)
        
if __name__ == "__main__":
    unittest.main()

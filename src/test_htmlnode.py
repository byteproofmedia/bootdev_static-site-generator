import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div","test",None,{"class": "test"})
        node_text = "HTMLNode(div, test, None, {'class': 'test'})"
        self.assertEqual(node.__repr__(), node_text)
    def test_child(self):
        child = HTMLNode("p","test",None,{"class": "child"})
        node = HTMLNode("div",None,[child],{"class": "test"})
        print(node.__repr__())
        node_text = "HTMLNode(div, None, [HTMLNode(p, test, None, {'class': 'child'})], {'class': 'test'})"
        self.assertEqual(node.__repr__(), node_text)
    def test_props_to_html(self):
        node = HTMLNode("div","test",None,{"class": "test"})
        props_text = " class=\"test\""
        self.assertEqual(node.props_to_html(), props_text)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_strong(self):
        node = LeafNode("strong", "Hello, world!")
        self.assertEqual(node.to_html(), "<strong>Hello, world!</strong>")

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!", {"class": "test"})
        self.assertEqual(node.to_html(), "<div class=\"test\">Hello, world!</div>")

    def test_leaf_to_html_none(self):
        node = LeafNode(None, "Hello, world!", {"class": "test"})
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()

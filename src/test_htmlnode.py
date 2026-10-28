import unittest
from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()

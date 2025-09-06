import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_exists(self):
        node = TextNode("https://this.is.link.node", TextType.LINK)
        node2 = TextNode(None, TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_type(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("https://www.boot.dev", TextType.LINK)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main() 

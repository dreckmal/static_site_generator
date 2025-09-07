import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = node_with_props = HTMLNode("a", "Click me!", None, {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(),  ' href="https://boot.dev" target="_blank"')


    def test_tag_value_assignment(self):
        node = HTMLNode(tag="p", value="This is some random paragraph.")
        self.assertIsNotNone(node.tag)
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is some random paragraph.")

    def test_tag_is_none_by_default(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)


if __name__ == "__main__":
    unittest.main()



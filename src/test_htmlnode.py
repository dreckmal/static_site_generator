import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_no_parent_value(self):
        child_node = LeafNode("b", "Hello Boss.")
        parent_node = ParentNode('p', [child_node])
        self.assertEqual(parent_node.value, None)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
            )

    def test_render_with_one_child(self):
        parent = ParentNode("div", [LeafNode("span", "x")])
        self.assertEqual(parent.to_html(), "<div><span>x</span></div>")

    def test_children_none_raises_in_to_html(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_multiple_children_order_preserved(self):
        child_a = LeafNode("b", "this one is bold")
        child_b = LeafNode("i", "This one is in italics")
        child_c = LeafNode(None, "this one is just text")
        parent = ParentNode("p", [child_a, child_b, child_c])
        self.assertEqual(parent.to_html(), "<p><b>this one is bold</b><i>This one is in italics</i>this one is just text</p>")

    def test_props_on_parent_render(self):
        parent = ParentNode("div", [LeafNode(None, "x")], {"class": "c", "id": "i"})
        self.assertEqual(parent.to_html(), '<div class="c" id="i">x</div>')


   
if __name__ == "__main__":
    unittest.main()



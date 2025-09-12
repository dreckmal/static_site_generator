from enum import Enum

from htmlnode import LeafNode
from textnode import TextType, TextNode
from text_to_html import text_node_to_html

def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

def test_text_bold(self):
    node = TextNode("This is a bold node", TextType.BOLD)
    html_node = text_node_to_html(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a bold node")

def test_text_italic(self):
    node = TextNode("This is a italic node", TextType.ITALIC)
    html_node = text_node_to_html(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a italic node")


def test_image(self):
    node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
    html_node = text_node_to_html(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(
        html_node.props,
        {"src": "https://www.boot.dev", "alt": "This is an image"},
    )















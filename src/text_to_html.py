from enum import Enum
from htmlnode import LeafNode
from textnode import TextType, TextNode

def text_node_to_html(text_node):
    if text_node is None:
        raise TypeError("text_node cannot be None")
    if not isinstance(text_node, TextNode):
        raise TypeError("text_node must be a TextNode.")
    if text_node.text_type is None:
        raise ValueError("unsupported TextType")

    if text_node.text_type == TextType.TEXT:
        if text_node.text is None:
            raise ValueError("TEXT requires text")
        return LeafNode(None, text_node.text)

    elif text_node.text_type == TextType.BOLD:
        if text_node.text is None:
            raise ValueError("BOLD requires text")
        return LeafNode('b', text_node.text)

    elif text_node.text_type == TextType.ITALIC:
        if text_node.text is None:
            raise ValueError("ITALIC requires text")
        return LeafNode('i', text_node.text)

    elif text_node.text_type == TextType.CODE:
        if text_node.text is None:
            raise ValueError("CODE requires text")
        return LeafNode('code', text_node.text)

    elif text_node.text_type == TextType.LINK:
        if text_node.text is None:
            raise ValueError("LINK requires text")
        if text_node.url is None:
            raise ValueError("URL requires a valid link")
        return LeafNode('a', text_node.text, props={'href':text_node.url})

    elif text_node.text_type == TextType.IMAGE:
        if text_node.text is None:
            raise ValueError("IMAGE requires alt text")
        if text_node.url is None:
            raise ValueError("IMAGE URL requires a valid link")
        return LeafNode('img', value="", props={"src":text_node.url, "alt":text_node.text})

    else:
        raise ValueError('unsupported TextType')



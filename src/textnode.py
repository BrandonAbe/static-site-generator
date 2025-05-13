from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE_TEXT = "code"
    LINK = 'link'
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return isinstance(other, TextNode) and self.text == other.text and self.text_type == other.text_type and self.url == other.url # Single line check

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case None:
            raise Exception("Text type not in Enum")
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url}) # a for anchor
        case TextType.IMAGE:
            if '|' in text_node.text:
                src, alt_text = text_node.text.split('|',1)
                return LeafNode("img", "", {"src": src, "alt": alt_text})
            else:
                return LeafNode("img", "", {"src": text_node.text, "alt": ""})
            #return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
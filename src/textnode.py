from enum import Enum

class TextType(Enum):
    NORMAL = 'normal'
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

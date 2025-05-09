from enum import Enum
from pydoc import text

class TextType(Enum):
    NORMAL = 'normal'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE_TEXT = "code"
    LINK = 'link'
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode): # Ensures comparison object is type(TextNode)
            if self.text == other.text and self.text_type == other.text_type and self.url == other.url: # If true, they match
                return True
            else:
                return False
        return False

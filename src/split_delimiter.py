from typing import Annotated
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list, delimiter: Annotated[str, "single character"], text_type: TextType):
    new_list = []
    for node in old_nodes:
        if delimiter not in node.text:
            raise Exception("Invalid Markdown: missing delimiter")
        if isinstance(node, TextNode):
            new_list.append(node)
    return new_list    
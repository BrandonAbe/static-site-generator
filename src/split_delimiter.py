from typing import Annotated
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list, delimiter: Annotated[str, "single character"], text_type: TextType):
    new_list = []
    for node in old_nodes:
        if delimiter not in node.text:
            raise Exception("Invalid Markdown: missing delimiter")
        # Keep unnchanged if not a TextNode
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        split_nodes = []

        # Split each "node" text based on delimiter
        sections = node.text.split(delimiter)

        '''
        Logic check: Does split lead to an even number of sections?
        If this happens (e.g. **text), an incorrect usage of delimiters has been used
        '''
        
        if len(sections) % 2 == 0:
            raise Exception("Invalid Markdown: missing closing delimiters")
        



    return new_list    
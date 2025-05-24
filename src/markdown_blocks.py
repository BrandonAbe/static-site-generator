from enum import Enum
from htmlnode import (
    ParentNode,
    LeafNode,
    )
from textnode import (
    text_node_to_html_node,
)
from inline_markdown import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"

def markdown_to_blocks(markdown):
    split_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        cleaned_block = block.strip() # Empty argument strips whitespace
        if cleaned_block != "":
            split_blocks.append(cleaned_block)
    return split_blocks

def block_to_block_type(block):
    lines = block.split("\n")
    
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")): # .startswith can take string or tuple. I use a tuple to check up to Heading 6
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"): # If open and closed with ```, then it is a code block. If length of lines is <=1, it's not a block.
        return BlockType.CODE
    if block.startswith(">"): # Check if quote
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):# Check if unordered list
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "): # Check if ordered list. Assumtion: All ordered lists will start with 1
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "): # If line is not any other enum, it is a paragraph
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

# Helper function
def text_to_children(text):
    text_nodes = text_to_textnodes(text) #splits text into each node type based on content
    children_html_nodes = []
    for text_node in text_nodes:
        children_html_nodes.append(text_node_to_html_node(text_node))
    return children_html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_node = None #Default

    if not blocks: # Return empty or whitespace input to return as empty div using LeafNode as ParentNode requires children
        return LeafNode("div", "")

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children = text_to_children(block)
            html_node = ParentNode("p",children)

        elif block_type == BlockType.HEADING: 
            heading_level = 0
            for char in block:
                if char == "#":
                    heading_level += 1
                else:
                    break
            heading_text = block[heading_level:].strip()
            children = text_to_children(heading_text)
            html_node = ParentNode(f"h{heading_level}",children)

        elif block_type == BlockType.CODE:
            code_content = block[3:-3]
            if code_content.startswith("\n"): # Handle if code content has new line at the start (edge case)
                code_content = code_content[1:]
            raw_code_leaf = LeafNode(None,code_content) # Assignment CH4_L3 requirement: "code" block shall not do any inline markdown parsing of it's children
            code_html = ParentNode("code",[raw_code_leaf])
            html_node = ParentNode("pre",[code_html]) # "pre" tag comes from CH4_L3 tip: "Code blocks should be surrounded by a <code> tag nested inside a <pre> tag."

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            processed_lines = []
            for line in lines:
                processed_line = line[1:].strip() # Removes ">" and whitespace
                processed_lines.append(processed_line)
            processed_text = "\n".join(processed_lines)
            children = text_to_children(processed_text)
            html_node = ParentNode("blockquote", children)

        elif block_type == BlockType.OLIST:
            lines = block.split('\n')
            list_items = []
            for i, line in enumerate(lines):
                 dot_index = line.find('.') # Using this index removes needing to worry about the ordered list leading number
                 space_index = line.find(' ', dot_index + 1)
                 item_text = line[space_index + 1:] # Everything after the space is content, except leading whitespace
                 children = text_to_children(item_text)
                 list_items.append(ParentNode("li", children))
            html_node = ParentNode("ol", list_items)

        elif block_type == BlockType.ULIST:
            lines = block.split('\n')
            list_items = []
            for line in lines:
                item_text = line[2:] # Removes leading number and "."
                children = text_to_children(item_text)
                list_items.append(ParentNode("li", children))
            html_node = ParentNode("ul", list_items)

        else:
            raise ValueError(f"Unknown block type: {block_type}")

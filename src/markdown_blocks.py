from enum import Enum

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
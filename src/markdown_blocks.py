def markdown_to_blocks(markdown):
    split_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        cleaned_block = block.strip() # Empty argument strips whitespace
        if cleaned_block != "":
            split_blocks.append(cleaned_block)
    return split_blocks
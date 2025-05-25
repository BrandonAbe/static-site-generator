import os

from markdown_blocks import (
    markdown_to_html_node
)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

def generate_page(from_path:str, template_path:str, dest_path:str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Handle markdown file
    from_file = open(from_path,"r") # Read-only mode
    markdown_content = from_file.read()
    from_file.close()

    # Handle template file
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    # Convert markdown to HTML Node and HTML string
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
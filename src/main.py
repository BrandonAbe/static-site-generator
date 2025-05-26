# Imports
import os
import shutil
from markdown_blocks import copy_files_recursive
from generate_content import generate_pages_recursive

# Variable definitions
dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

# Main function definition
def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path,dir_path_public)

# Start main() loop
main()

# Imports
import os
import shutil
from markdown_blocks import copy_files_recursive

# Variable definitions
dir_path_static = "./static"
dir_path_public = "./public"

# Main function definition
def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


# Start main() loop
main()

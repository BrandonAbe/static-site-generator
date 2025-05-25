import unittest
from markdown_blocks import (
    markdown_to_html_node
)
from generate_content import (
    extract_title,
)

class TestExtractTitle(unittest.TestCase):
    def test_title_exists(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_two_titles_exists(self):
        actual = extract_title(
            """
# Title number one

# Title number two, that should be ignored
"""
        )
        self.assertEqual(actual, "Title number one")

    def test_no_title(self):
        try:
            extract_title (
"""
no heading character, no title
 """           
        )
        except: 
            Exception("No title")
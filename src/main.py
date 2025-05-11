from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode

# Main function definition
def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    html_node = HTMLNode("div", "Hello, Boot.dev!", None, {"class": "greeting", "href": "https://boot.dev"},)

# Start main() loop
main()

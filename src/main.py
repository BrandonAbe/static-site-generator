from textnode import TextNode
from textnode import TextType

# Main function definition
def main():
    text_node = TextNode("This is some anchor text",TextType.LINK,"https://www.boot.dev")
    print(text_node)

# Start main() loop
main()

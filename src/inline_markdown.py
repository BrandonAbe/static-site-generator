from typing import Annotated
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        # If not a text node, add it unchanged
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        # Process text nodes
        current_text = old_node.text
        remaining_text = current_text
        result_nodes = []
        
        # opening delimiter
        while delimiter in remaining_text:
            start_index = remaining_text.find(delimiter)
            
            if start_index > 0: # If there's text before the delimiter, add it as a TEXT node
                result_nodes.append(TextNode(remaining_text[:start_index], TextType.TEXT))
                
            remaining_text = remaining_text[start_index + len(delimiter):] 
            end_index = remaining_text.find(delimiter) # Find the closing delimiter
            
            # If no closing delimiter, raise an exception
            if end_index == -1:
                raise Exception(f"Invalid Markdown: missing closing delimiter '{delimiter}'")
                

            delimited_content = remaining_text[:end_index]
            result_nodes.append(TextNode(delimited_content, text_type))  # Extract the content between delimiters
            
            remaining_text = remaining_text[end_index + len(delimiter):] # Continue with the rest of the text
        
        # Add any remaining text as a TEXT node
        if remaining_text:
            result_nodes.append(TextNode(remaining_text, TextType.TEXT))
        
        new_nodes.extend(result_nodes)
    
    return new_nodes
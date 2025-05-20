from typing import Annotated
from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes:list, delimiter:str, text_type:enumerate):
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
            start_index = remaining_text.find(delimiter) #returns lowest index of found delimiter, returns -1 if not found
            
            if start_index > 0: # If there's text before the delimiter, add it as a TEXT node
                result_nodes.append(TextNode(remaining_text[:start_index], TextType.TEXT)) # Grab everything before start index, set to TEXT type and add to result_nodes
                
            remaining_text = remaining_text[start_index + len(delimiter):] #skip over delimiter we just found
            end_index = remaining_text.find(delimiter) # Find the closing delimiter
            
            # If no closing delimiter, raise an exception
            if end_index == -1:
                raise Exception(f"Invalid Markdown: missing closing delimiter '{delimiter}'")
                

            delimited_content = remaining_text[:end_index] # text between delimiters
            result_nodes.append(TextNode(delimited_content, text_type))  # add text between delimiters to result, along with text_type
            remaining_text = remaining_text[end_index + len(delimiter):] # Continue with the rest of the text
        
        # Add any remaining text as a TEXT node
        if remaining_text:
            result_nodes.append(TextNode(remaining_text, TextType.TEXT))
        
        new_nodes.extend(result_nodes)
    
    return new_nodes

def extract_markdown_images(text: str):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text: str):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern,text)
    return matches
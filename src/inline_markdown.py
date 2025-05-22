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

def split_nodes_image(old_nodes: list):
    new_nodes = []
    
    for old_node in old_nodes:
        # If not a text node, add it unchanged
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        # Split up each node in old_nodes
        original_text = old_node.text
        images = extract_markdown_images(original_text)
    
        if len(images) == 0: # If no image pattern found
            new_nodes.append(old_node)
            continue

        for image in images:
            '''
            Logic: for each image string in images, create a list of sections. 
            That list shall contain text from the original_text, split by the markdown formatting instead of a delimiter.
            This splitting should only occur once. Recall the output of extract_markdown_images is a tuple,
            where the first [0] element is the "alt text" and second [1] element is the "image_url".
            ''' 
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1) 
            if len(sections) != 2: #If not exactly 2 sections exist,
                raise Exception("Invalid Markdown: Image section not closed")
            if sections[0] != "": # If there is text before the image, add it as regular TEXT node
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            #otherwise append TextNode of the image
            new_nodes.append(TextNode(image[0], TextType.IMAGE,image[1]))
            original_text = sections[1]
            '''
            Logic: I set original_text to the second half of the split to allow for situations where multiple
            images are contained within the text (i.e. "This is ![one](url1) and ![two](url2)").
            Without overwriting original_text, the next iteration of the loop would split the same original text
            instead of progressing to the next image's alt text.
            '''
        if original_text != "": #if there is a link remaining...
            new_nodes.append(TextNode(original_text,TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes): # Similar to split_nodes_image, but for links
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        links = extract_markdown_links(original_text)

        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid Markdown: Link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
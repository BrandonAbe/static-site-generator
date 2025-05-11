from enum import Enum

class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None):
        '''
        tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        children - A list of HTMLNode objects representing the children of this node
        props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        '''
        
        self.tag:str = tag
        self.value:str = value
        self.children:list = children
        self.props:dict = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        # Only one None in memory ever, so can use "is" to check 
        # if memory of self.props matches None location
        if self.props is None: 
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"' # Match formatting of CH2L3 step 5
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag:str, value:str, props:dict=None):
        super().__init__(tag, value, props)
        self.tag:str = tag
        self.value:str = value
        self.props:dict = props
        
    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value defined")
        if self.tag is None:
            return self.value 
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
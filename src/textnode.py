from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, type, value="", **kwargs):
        self.value = value
        self.type = type
        # Store additional properties, like src, alt, or href
        self.props = kwargs

    def __eq__(self, other):
        return self.value == other.value and self.type == other.type and self.props == other.props
    
    def __repr__(self):
        return f"TextNode({self.value}, {self.type.value}, {self.props})"
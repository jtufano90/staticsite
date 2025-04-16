from textnode import TextNode, TextType
from htmlnode import LeafNode

TYPE_TO_TAG_MAP = {
    TextType.TEXT: None,
    TextType.BOLD: "b",
    TextType.ITALIC: "i",
    TextType.CODE: "code",
    TextType.LINK: {"tag": "a", "props": ["href"]},
    TextType.IMAGE: {"tag": "img", "props": ["src", "alt"]},
}

def text_node_to_html_node(text_node):
    tag_info = TYPE_TO_TAG_MAP.get(text_node.type)

    if tag_info is None:
        # Handle TextType.TEXT case
        return LeafNode(tag=None, value=text_node.value)

    elif isinstance(tag_info, str):
        # Handle simple tags like "b", "i", "code"
        return LeafNode(tag=tag_info, value=text_node.value)

    elif isinstance(tag_info, dict):
        # Handle special cases like LINK and IMAGE
        tag = tag_info["tag"]
        # Get properties from text_node.props
        props = {}
        for prop in tag_info.get("props", []):
            if prop in text_node.props:
                props[prop] = text_node.props[prop]
            else:
                props[prop] = ""
        
        return LeafNode(tag=tag, value=text_node.value, props=props)

    else:
        # Raise an exception for unsupported TextType
        raise ValueError(f"Unsupported TextType: {text_node.type}. Please make sure your TextType is valid.")
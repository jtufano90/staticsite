class HTMLNode():
    def __init__(self, tag=None, value=None, props=None, children=None):
        self.tag = tag
        self.value = value
        self.props = props if props else {}

        if children is not None:
            self.children = children

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        prop_string = ""
        if self.props == None:
            return ""
        for key in self.props:
            prop_string += f' {key}="{self.props[key]}"'
        return prop_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None,):
        # Ensure the LeafNode must have a value
        if value is None:
            raise ValueError("LeafNode must have a value.")
        
        # Call superclass's constructor
        super().__init__(tag, value, props, children=None)

    @property
    def children(self):
        # Prevent access to children
        raise Exception("LeafNode does not support children.")

    @children.setter
    def children(self, value):
        # Prevent assigning children
        raise Exception("LeafNode cannot have children.")
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        
        if self.tag is None:
            return self.value  # Return raw text if there's no tag

        # Handle props (attributes)
        props_string = ""
        if self.props:  # Only process props if they exist
            props_string = " " + " ".join([f'{key}="{value}"' for key, value in self.props.items()])

        # Return properly formatted HTML
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, props=props, children=children)

    def to_html(self):
        # Check for tag.
        if self.tag is None:
            raise ValueError("ParentNode must have a tag.")
        # Check for children
        if not hasattr(self, 'children'):  # A safer check
            raise ValueError("ParentNode must have children.")
        
        # Opening tag.
        html = f"<{self.tag}"

        # Add props if they exist.
        if self.props is not None:
            for prop_name, prop_value in self.props.items():
                html += f' {prop_name}="{prop_value}"'

        html += ">"

        # Add children.
        for child in self.children:
            html += child.to_html()

        # Closing tag.
        html += f"</{self.tag}>"

        return html

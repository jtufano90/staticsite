import unittest

from convert import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestTextNodeToHtmlNode(unittest.TestCase):

    def test_image_props(self):
        # Create a TextNode of type IMAGE
        text_node = TextNode(src="image.jpg", alt="A description", type=TextType.IMAGE)
        
        # Convert it using the function
        html_node = text_node_to_html_node(text_node)
        
        # Assert the "props" dictionary is constructed properly
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")  # Images have no value
        self.assertEqual(html_node.props["src"], "image.jpg")
        self.assertEqual(html_node.props["alt"], "A description")

    def test_link_props(self):
        # Create a TextNode of type LINK
        text_node = TextNode(href="https://example.com", value="Click Here", type=TextType.LINK)
        
        # Convert it using the function
        html_node = text_node_to_html_node(text_node)
        
        # Assert the "props" dictionary is constructed properly
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_missing_props(self):
        # Create a malformed TextNode without the alt property for an IMAGE
        text_node = TextNode(src="image.jpg", type=TextType.IMAGE)
        
        # Convert it using the function
        html_node = text_node_to_html_node(text_node)
        
        self.assertEqual(html_node.tag, "img")  # Images use the <img> tag
        self.assertEqual(html_node.value, "")   # Images have empty value
        self.assertEqual(html_node.props, {"src": "image.jpg", "alt": ""})  # Missing alt defaults to empty string

if __name__ == "__main__":
    unittest.main()
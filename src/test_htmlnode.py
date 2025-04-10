import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        # Test with empty props (None)
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_single_prop(self):
        # Test with a single property
        node = HTMLNode(props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')
        
    def test_props_to_html_multiple_props(self):
        # Test with multiple properties
        node = HTMLNode(props={
            "href": "https://example.com",
            "target": "_blank",
            "class": "link"
        })
        # The order of attributes might vary, so we'll check for each one
        result = node.props_to_html()
        self.assertIn(' href="https://example.com"', result)
        self.assertIn(' target="_blank"', result)
        self.assertIn(' class="link"', result)
        # Check the total length to ensure we don't have extra spaces
        self.assertEqual(
            len(result), 
            len(' href="https://example.com" target="_blank" class="link"')
        )

if __name__ == "__main__":
    unittest.main()
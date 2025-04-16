import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_with_tag(self):
        node = LeafNode("p", "Hello world!")
        self.assertEqual(node.to_html(), "<p>Hello world!</p>")

    def test_leaf_to_html_with_tag_and_props(self):
        node = LeafNode("a", "Click me", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("span", None).to_html()

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
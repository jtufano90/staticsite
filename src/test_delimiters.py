import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_basic(self):
        # Test with a simple code block
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        # Expected result
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        
        # Check the length
        self.assertEqual(len(new_nodes), len(expected))
        
        # Check each node's content and type
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i].value, expected[i].value)
            self.assertEqual(new_nodes[i].type, expected[i].type)
    
    def test_split_nodes_delimiter_multiple(self):
        # Test with multiple code blocks
        node = TextNode("Text with `code1` and `code2` blocks", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
        expected = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("code1", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("code2", TextType.CODE),
            TextNode(" blocks", TextType.TEXT),
        ]
        
        self.assertEqual(len(new_nodes), len(expected))
        for i in range(len(new_nodes)):
            self.assertEqual(new_nodes[i].value, expected[i].value)
            self.assertEqual(new_nodes[i].type, expected[i].type)
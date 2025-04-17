from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    
    for old_node in old_nodes:
        if old_node.type == TextType.TEXT:
            text = old_node.value
            
            # Find all delimiter pairs
            parts = []
            remaining_text = text
            
            while delimiter in remaining_text:
                # Find the first delimiter
                start_index = remaining_text.find(delimiter)
                if start_index == -1:
                    break
                
                # Find the second delimiter
                end_index = remaining_text.find(delimiter, start_index + len(delimiter))
                if end_index == -1:
                    raise ValueError(f"Unclosed delimiter: {delimiter}")
                
                # Extract the parts
                before = remaining_text[:start_index]
                content = remaining_text[start_index + len(delimiter):end_index]
                
                # Add parts to result
                if before:
                    parts.append((before, TextType.TEXT))
                parts.append((content, text_type))
                
                # Update remaining text
                remaining_text = remaining_text[end_index + len(delimiter):]
            
            # Add any remaining text
            if remaining_text:
                parts.append((remaining_text, TextType.TEXT))
            
            # Create TextNode objects and add to result
            for text_content, node_type in parts:
                result.append(TextNode(text_content, node_type))
        else:
            # If not a text node, add as is
            result.append(old_node)
    
    return result
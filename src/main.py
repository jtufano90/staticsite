from textnode import TextNode, TextType

def main():
    node = TextNode("Test", TextType.BOLD, None)
    print(repr(node))

if __name__ == "__main__":
    main()
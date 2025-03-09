import unittest
from text_to_html_processor import text_node_to_html_node
from textnode import TextNode
from textnode import TextType


class Test_Text_To_HTML(unittest.TestCase):

    # Test the conversion of TextNode with TextType.NORMAL to LeafNode
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    # Test the conversion of TextNode with TextType.BOLD to LeafNode with <b> tag
    def test_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

    # Test the conversion of TextNode with TextType.ITALIC to LeafNode with <i> tag
    def test_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")

    # Test the conversion of TextNode with TextType.CODE to LeafNode with <code> tag
    def test_code(self):
        node = TextNode("Code snippet", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code snippet")

    # Test the conversion of TextNode with TextType.LINK to LeafNode with <a> tag and href attribute
    def test_link(self):
        node = TextNode("Click here", TextType.LINK, "http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props["href"], "http://example.com")

    # Test the conversion of TextNode with TextType.IMAGE to LeafNode with <img> tag and src/alt attributes
    def test_image(self):
        node = TextNode("Image alt text", TextType.IMAGE, "http://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "http://example.com/image.jpg")
        self.assertEqual(html_node.props["alt"], "Image alt text")

    # Test that ValueError is raised if LINK type TextNode has no URL
    def test_invalid_link(self):
        node = TextNode("Invalid link", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    # Test that ValueError is raised if IMAGE type TextNode has no URL
    def test_invalid_image(self):
        node = TextNode("Invalid image", TextType.IMAGE)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    # Test that ValueError is raised for unsupported TextType
    def test_invalid_text_type(self):
        node = TextNode("Unsupported text type", TextType.NORMAL)
        node.text_type = "INVALID"  # Modify to an invalid type
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    if __name__ == "__main__":
        unittest.main()

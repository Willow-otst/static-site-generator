import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    
    # Test equality of two TextNode objects
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    # Test inequality of two TextNode objects (different text)
    def test_eq_diff_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    # Test inequality of two TextNode objects (different text type)
    def test_eq_diff_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    # Test inequality of two TextNode objects (different URL)
    def test_eq_diff_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://different-url.com")
        self.assertNotEqual(node, node2)

    # Test the __repr__ method to check the correct string representation
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        expected_repr = "TextNode(This is a text node, BOLD, None)"
        self.assertEqual(repr(node), expected_repr)

    # Test the __repr__ method with a URL
    def test_repr_with_url(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        expected_repr = "TextNode(Click here, LINK, https://example.com)"
        self.assertEqual(repr(node), expected_repr)
    
    # Test that URL is None when not passed
    def test_url_is_none_when_not_passed(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)

if __name__ == "__main__":
    unittest.main()

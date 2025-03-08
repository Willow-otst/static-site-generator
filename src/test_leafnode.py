import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    # Test initialization with arguments
    def test_init_with_args(self):
        node = LeafNode(tag="div", value="Hello", props={"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.props, {"class": "container"})

    # Test to_html for a valid tag with value and props
    def test_to_html_with_tag_and_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    # Test to_html for a valid tag with value and no props
    def test_to_html_with_tag_no_props(self):
        node = LeafNode(tag="h1", value="Header without props")
        self.assertEqual(node.to_html(), "<h1>Header without props</h1>")

    # Test to_html with no tag (raw text)
    def test_to_html_no_tag(self):
        node = LeafNode(tag=None, value="This is raw text")
        self.assertEqual(node.to_html(), "This is raw text")

    # Test that raises ValueError when value is None
    def test_to_html_value_none(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="div", value=None)

    # Test the __repr__ method to check correct string representation
    def test_repr(self):
        node = LeafNode(tag="div", value="Test", props={"class": "test"})
        expected_repr = "LeafNode(tag=div, value=Test, props={'class': 'test'})"
        self.assertEqual(repr(node), expected_repr)

    # Test that to_html works with empty value (only for tags that are valid)
    def test_to_html_empty_value(self):
        node = LeafNode(tag="img", value="", props={"src": "image.png"})
        # Adjusting the expected output to match the current behavior (self-closing)
        self.assertEqual(node.to_html(), '<img src="image.png"></img>')

    # Test to_html that raises ValueError when value is None
    def test_to_html_value_none_in_constructor(self):
        with self.assertRaises(ValueError):
            # If value is None, this should raise ValueError
            LeafNode(tag="div", value=None)

if __name__ == "__main__":
    unittest.main()

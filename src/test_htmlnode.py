import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    # Test initialization with no arguments
    def test_init_with_no_args(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    # Test initialization with specific arguments
    def test_init_with_args(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "container"})

    # Test the props_to_html method to verify correct conversion to attributes
    def test_props_to_html(self):
        node = HTMLNode(tag="div", value=None, children=[], props={"class": "container", "id": "main"})
        props_html = node.props_to_html()
        self.assertEqual(props_html, ' class="container" id="main"')

    # Test the __repr__ method to check correct string representation
    def test_repr(self):
        node = HTMLNode(tag="div", value="Test", children=[], props={"class": "test"})
        expected_repr = 'HTMLNode(tag=div, value=Test, children=[], props={\'class\': \'test\'})'
        self.assertEqual(repr(node), expected_repr)

    # Test that calling to_html on the base class raises NotImplementedError
    def test_to_html_not_implemented(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "container"})
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    # Test that returning properties are an empty string when initialized to None
    def test_props_to_html_empty_props(self):
        node = HTMLNode(tag="span", props={})
        props_html = node.props_to_html()
        self.assertEqual(props_html, "")

    # Test that verifies the existence and value of child node
    def test_node_with_children(self):
        child = HTMLNode(tag="span", value="child")
        node = HTMLNode(tag="div", children=[child])
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].value, "child")

    # Test that Node with children print as human readable when nested
    def test_repr_with_children(self):
        child = HTMLNode(tag="span", value="child_text")
        node = HTMLNode(tag="div", children=[child])
        expected_repr = (
            "HTMLNode(tag=div, value=None, children=[HTMLNode(tag=span, value=child_text, children=[], props={})], props={})"
        )
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()

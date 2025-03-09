import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    
    # Test the to_html method when there is one child node
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    # Test the to_html method when there are nested child and grandchild nodes
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    # Test the to_html method with multiple children
    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("p", "First child")
        child_node2 = LeafNode("p", "Second child")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><p>First child</p><p>Second child</p></div>")

    # Test the to_html method when no tag is provided
    def test_to_html_with_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "Child without tag")])

    # Test the to_html method when no children are provided
    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    # Test the to_html method when the children argument is None
    def test_to_html_with_no_children_provided(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    # Test the to_html method with nested ParentNode objects
    def test_to_html_with_nested_parent_nodes(self):
        child_node = LeafNode("p", "Child text")
        parent_node = ParentNode("section", [child_node])
        grandparent_node = ParentNode("div", [parent_node])
        self.assertEqual(grandparent_node.to_html(), "<div><section><p>Child text</p></section></div>")

    # Test the __repr__ method to check the string representation of ParentNode
    def test_repr(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        expected_repr = "ParentNode(tag=div, children=[LeafNode(tag=span, value=child, props={})], props={})"
        self.assertEqual(repr(parent_node), expected_repr)

    # Test the to_html method with props (HTML attributes)
    def test_to_html_with_props(self):
        child_node = LeafNode("a", "Click me", {"href": "https://www.example.com", "class": "link"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><a href="https://www.example.com" class="link">Click me</a></div>')

if __name__ == "__main__":
    unittest.main()

from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag.")
        if not children:
            raise ValueError("ParentNode must have children.")

        super().__init__(tag, value=None, children=children, props=props)
    
    def to_html(self):
        children_html = "".join([child.to_html() for child in self.children])

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"
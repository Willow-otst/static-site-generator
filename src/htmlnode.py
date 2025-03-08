class HTMLNode:
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        # This will be overridden by child classes.
        raise NotImplementedError("Subclasses should implement this method.")

    def props_to_html(self):
        # Convert the props dictionary into HTML attribute format
        return ''.join([f' {key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        # Return a string representation of the HTMLNode
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

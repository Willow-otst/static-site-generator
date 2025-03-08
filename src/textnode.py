from enum import Enum

# types of handleable text
class TextType(Enum):
    NORMAL = "NORMAL"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"

# definition of a node of text
class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # check of if two objects are equal
    def __eq__(self, other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    # human readable representation of object
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
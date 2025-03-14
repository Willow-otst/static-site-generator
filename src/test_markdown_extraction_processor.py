import unittest
from markdown_extraction_processor import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):
    # Test the extraction of markdown images
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertEqual(matches, [("image", "https://i.imgur.com/zjjcJKZ.png")])

    # Test the extraction of markdown links
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertEqual(matches, [("to boot dev", "https://www.boot.dev"), 
                                   ("to youtube", "https://www.youtube.com/@bootdotdev")])

    # Test when there are no images in the markdown text
    def test_no_images(self):
        text = "This is just a plain text without images."
        matches = extract_markdown_images(text)
        self.assertEqual(matches, [])

    # Test when there are no links in the markdown text
    def test_no_links(self):
        text = "This is just a plain text without links."
        matches = extract_markdown_links(text)
        self.assertEqual(matches, [])

    # Test when the markdown contains both links and images
    def test_images_and_links(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link [to google](https://www.google.com)"
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)
        
        self.assertEqual(image_matches, [("image", "https://i.imgur.com/zjjcJKZ.png")])
        self.assertEqual(link_matches, [("to google", "https://www.google.com")])

if __name__ == "__main__":
    unittest.main()

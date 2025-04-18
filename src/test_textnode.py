import unittest


from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_edge_url(self):
        node = TextNode("holi", TextType.LINK)
        node2 = TextNode("holi", TextType.LINK, "python.org")
        self.assertNotEqual(node, node2)

    def test_text_prop(self):
        node = TextNode("holi", TextType.BOLD)
        node2 = TextNode("holi", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_txt_diff(self):
        node = TextNode("holi", TextType.TEXT)
        node2 = TextNode("different_text", TextType.TEXT)
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()

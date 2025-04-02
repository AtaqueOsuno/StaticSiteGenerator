# hello world
from textnode import TextNode, TextType

def main():
    holi = TextNode("holi", TextType.LINK, "google.com")
    print(holi)


# Using the special variable
# __name__
if __name__=="__main__":
    main()

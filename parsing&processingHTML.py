from html.parser import HTMLParser

import parser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered a comment:", data)
        pos = self.getpos()
        print("At line:", pos[0], "position", pos[1])

    def handle_starttag(self, tag, attrs):
        pass

    def handle_data(self, data):
        pass


def main():
    parser = MyHTMLParser()


f = open("samplehtml.html")
if f.mode == "r":
    contents = f.read()  # read the entire file
    parser.feed(contents)

if __name__ == "__main__":
    main()

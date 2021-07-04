from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    scraped = []
    lookFor = ['you', 'programmer']

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        parts = data.split()

        self.scraped.append(''.join([data for part in self.lookFor if part in parts]))
        self.scraped = [item for item in self.scraped if item != '']
        print(self.scraped)

    def get_scraped_data(self):
        return ' '.join(self.scraped)


parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>a programmer is an idiot</h1> <h1>you are an idiot also</h1> </body></html>')

print(parser.get_scraped_data())

if __name__ == '__main__':
    pass

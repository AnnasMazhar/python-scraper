from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):


    def __init__(self,base_url,page_url):
        # calling the parent class
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        # a tag contains the link so searching the webpage for a tag
        if tag == 'a':
            for (attribute,value) in attrs:
                # the a tag contains "href" attribute which holds the links
                if attribute == 'href':
                    url = parse.urljoin(self.base_url,value)
                    self.links.add(url)


    def page_links(self):
        # returning the links
        return self.links

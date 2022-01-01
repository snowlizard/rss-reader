from bs4 import BeautifulSoup
import requests


class ReadRSS:
    '''Class for reading RSS Feeds only takes
    one argument. The URL of a feed'''
    def __init__(self, url) -> None:
        '''Initializes class returns None'''
        self.url = url
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content, "html5lib",
                                  from_encoding="utf-8")

    def getTitles(self):
        '''Prints all the titles from the given rss url
        and returns that title'''
        temp = []
        titles = self.soup.find_all("title")
        for i in range(2, len(titles)):
            temp.append(titles[i].text)
        self.page.close()
        return temp

    def getContent(self, t):
        '''Takes the title (t) of an article and prints the aritcles
        content to the screen.'''
        title = self.soup.find(string=t)
        parent = title.findParent("title").findParent("item")
        self.page.close()
        return parent.prettify()

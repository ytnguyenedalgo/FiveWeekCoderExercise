import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        with open('output.txt', 'w') as f:
            for tag in sp.find_all("a"):
                url = tag.get("href")
                if url is None:
                    continue
                if url in url:
                    result = "\n" + url
                    f.write(result)

news = 'http://news.google.com/'
Scraper(news).scrape()

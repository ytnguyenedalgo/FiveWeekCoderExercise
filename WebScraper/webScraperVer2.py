import requests 
from bs4 import BeautifulSoup


class Scraper():
    def __init__(self, site):
        self.site = site


    def scrape(self):
        page = requests.get(self.site)

        #to check if the site is successfully 
        #loaded. A status code starting with
        #a 2 usually incates success while 4
        #or 5 indicates error.
        print(page.status_code)
        
        page_content = page.content
        parser = 'html.parser'
        soup = BeautifulSoup(page_content, parser)
        
        with open('outputVer2.txt', 'w') as f:
            for tag in soup.find_all('a', href=True):
                url = tag['href']
                if url is None:
                    continue
                else:
                    result="\n {}".format(url)
                    f.write(result)


news = "http://news.google.com/"
Scraper(news).scrape()


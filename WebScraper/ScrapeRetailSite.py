
# coding: utf-8

# In[2]:


"""
Build a web scraper for one of the websites: macys.com.

Author: Ye N.E.

Description: 
    (1) The web scraper should scrape Macys.com 
        whenever you run your program, scrape all of the products 
        listed on Macy's homepage, 
        and save the following data for each product 
        in a CSV file: the product name, price, and description.
    
    (2) The information should come from the product pages 
        (such as here: https://mcys.co/2GiLTRq)
        
    (3) Your program needs a function that allows me to search 
        by name all of the products in the CSV file. 
        If a product is found, your program should print 
        the product name, price, and description. 
"""

from bs4 import BeautifulSoup as Soup
import requests
import urllib.request
import re
import csv
import apikey


class Products:
    def __init__(self):
        self.names = []
        self.prices = []
        self.descriptions = []
        self.product_names = {}

        
class GetParse():
    def __init__(self, site):
        self.site = site 
        self.agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        api_key = apikey.Key()
        self.payload = {'api_key':api_key, 'url':'https://httpbin.org/ip'}
        #comment out the line below if you use Scraper API
        self.page = requests.get(self.site, headers=self.agent)
        #comment out the line below if you dont't want to use Scraper API
        #self.page = requests.get(self.site, params=self.payload, timeout=60) 
        self.soup = Soup(self.page.content, "html.parser")
    
    
    def __repr__(self):
        
        return self.page.status_code, self.text

        
class Scraper: 
    def __init__(self, site="https://www.macys.com"):
        self.site = site 
        self.Categories = set()
        self.URLs = set()
        self.productName = []
        self.productPrice = []
        self.productDesc = []
        self.products = []
    

    def get_url_categories(self):
        soup = GetParse(self.site).soup
        print(soup)
        for tag in soup.find_all("a", href=True):
            path = tag["href"]
            if "http" not in path                and "COL" in path                and "/shop/" in path:
                self.Categories.add(self.site+path)
        
        return self.Categories
    
    
    def get_url_products(self):
        self.get_url_categories()
        test = self.Categories.pop()
        self.Categories.add(test)
        soup = GetParse(test).soup
        for url in self.Categories:
            soup = GetParse(test).soup
            for tag in soup.find_all("a", {"class": "productDescLink"}):
                path = tag.get("href")
                self.URLs.add(self.site+path)
        
        return self.URLs
            
        
    def scrape(self):
        self.get_url_products()
        for url in self.URLs:
            soup = GetParse(url).soup
            name = ((soup.find_all("h1", {"class": "p-name h3"})[0].text)                    .replace("\n","")).strip()
            price = ((soup.find_all("div", {"class": "price"})[0].text)                     .replace("\n","")).strip()
            des = ((soup.find_all("p", {"data-auto": "product-description"})[0].text)                   .replace("\n","")).strip()
            self.productName.append(name)
            self.productPrice.append(price)
            self.productDesc.append(des)
            self.products.append([name, price, des])
            
        return self.products
    
    
    def save_cvs(self):
        self.scrape()
        with open("macys-products.cvs", "w+") as csvf:
            w = csv.writer(csvf, delimiter=",")
            for i in self.products:
                w.writerow(i)
            
    
scrape = Scraper()         
#scrape.get_url_products()
#scrape.scrape()
scrape.save_cvs()


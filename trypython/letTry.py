from requests import get
from selenium import webdriver
import json
import pprint
from webScraping import simple_get
from bs4 import BeautifulSoup as soup
myURL = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

url = get(myURL, headers=headers)
html = soup(url.content, 'html.parser')
#html.find_all("div", class_="rs-property-address ellipsis") is to find by class.

divs = html.find(id = 'getting-help')
print(divs)

#I SHALL LEAVE THIS UNFINISHED BECAUSE THIS IS AN INCREDIBLE HEADEACH HOWEVER IT WAS NOT THE CASE THAT IT WAS A FALURE SINCE I CAME OUT LEARNONG MORE ABOUT PYTHON AN
#AND WEBSCRAPING onto the next.
# print(html.prettify())
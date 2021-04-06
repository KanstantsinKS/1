# http://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup

responce = requests.get('http://quotes.toscrape.com/')
# print(responce.text)

html_data = BeautifulSoup(responce.text, 'html.parser')
quotes = html_data.find_all(class_='quote')


for quote in quotes:
    print('Quote: ' + quote.find(class_='text').get_text())
    print('By: ' + quote.find(class_='author').get_text())
    print('Tags: ' + quote.find(class_='keywords')['content'])
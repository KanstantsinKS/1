# http://quotes.toscrape.com/

import requests
from bs4 import BeautifulSoup
import csv

responce = requests.get('http://quotes.toscrape.com/')
# print(responce.text)

html_data = BeautifulSoup(responce.text, 'html.parser')
quotes = html_data.find_all(class_='quote')


with open('quotes.csv', 'w', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Quote', 'Author', 'Tags'])
    for quote in quotes:
        quote_text = (quote.find(class_='text').get_text())
        author = (quote.find(class_='author').get_text())
        tags = (quote.find(class_='keywords')['content'])
        csv_writer.writerow([quote_text, author, tags])




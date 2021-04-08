import requests

url = 'http://google.com/asda'
res = requests.get(url)
print(f'Requests to {url}. Status code is {res.status_code}.')

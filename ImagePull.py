## Name: Max Friedlander
## Location: Los Angeles
## Date: 10-25-2020

from bs4 import BeautifulSoup

import requests

response = requests.get(
    'https://www.artstation.com/?sort_by=community')  #artstation site
if response.status_code == 200:
    print('Success')
elif response.status_code == 404:
    print('Failure')

source = requests.get('https://www.artstation.com/?sort_by=community').text

soup = BeautifulSoup(source, 'lxml')

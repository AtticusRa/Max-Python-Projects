## Name: Max Friedlander
## Location: Los Angeles
## Date: 10-25-2020

from bs4 import BeautifulSoup
import requests
import os

BASE_URL = 'https://www.artstation.com/'  #search?q=input

# The User-Agent request header contains a characteristic string
# that allows the network protocol peers to identify the application type,
# operating system, and software version of the requesting software user agent.
# needed for google search
usr_agent = {
    'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

SAVE_FOLDER = 'artstation-images'


def main():
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    download_images()


def download_images():
    #ask user for search term and amount of images
    data = input('What are you looking for? ')
    n_images = int(input('How many images do you want? '))

    #create search url and request
    searchURL = BASE_URL + 'q=' + data + 'sort_by=relevance'
    response = requests.get(searchURL, headers=usr_agent)
    ## html = response.text

    #create soup object from response
    soup = BeautifulSoup(response.text, 'html.parser')

    #find all gallery grid links from search page
    results = soup.find_all('a', href=True)

    #sort links into a list
    galleryLinks = []
    for link in results:
        print(link['href'])


if __name__ == '__main__':
    main()

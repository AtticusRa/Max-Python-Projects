#Max Friedlander
#testing requests and bs4
import requests, re
from bs4 import BeautifulSoup as bs

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

#create response object from URL / load the webpage content
response = requests.get('https://www.artstation.com/artwork/WKGbrG',
                        headers=usr_agent)

#convert response object to beautifulsoup object
soup = bs(response.content, 'lxml')

print(soup.prettify())

first_header = soup.find('h2')
header_h2 = soup.find_all('h2')
headers = soup.find_all(['h3', 'h2', 'h1'])
#print(*headers, sep='\n')

body = soup.find('body')
div = body.find('div')
header = div.find('h1')

paragraphs = soup.find('p', string=re.compile('Some'))
headers2 = soup.find('h2', string=re.compile('(H|h)eader'))
#print(paragraphs, headers2)

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(*links, sep='\n')

#need to figure out to how to satisfy captcha requests on pages like artstation, you know in an okay way.

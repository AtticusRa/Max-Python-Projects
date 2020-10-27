""" #Sample code 1

import requests  # to get image from the web
import shutil  # to save it locally

## Set up the image URL and filename
image_url = "https://pixabay.com/get/52e8d7404c53ae14f6d1867dda353678153cd8ec53507448_1920.jpg"
filename = image_url.split("/")[-1]

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream=True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True

    # Open a local file with wb ( write binary ) permission.
    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    print('Image sucessfully Downloaded: ', filename)
else:
    print('Image Couldn\'t be retreived')
    
    
    
url = "http://www.reddit.com/r/BabyYoda"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

images = soup.find_all("img", attrs={'alt': 'Post Image'})

number = 0

for image in images:
    image_src = image['src']
    print(image_src)
    urllib.request.urlretrieve(image_src, str(number))
    number += 1
     """
    
""" #get the data
data = requests.get('https://umggaming.com/leaderboards')

#load data into bs4
soup = BeautifulSoup(data.text, 'lxml')

leaderboard = soup.find('table', {'id': 'leaderboard-table'})
tbody = leaderboard.find('tbody')

for tr in tbody.find_all('tr'):
    place = tr.find_all('td')[0].text.strip()
    username = tr.find_all('td')[1].find_all('a')[1].text.strip()
    xp = tr.find_all('td')[4].text.strip()
    print(place, username, xp)
 """ """
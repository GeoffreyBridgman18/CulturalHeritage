import requests
import cloudscraper
from bs4 import BeautifulSoup

i = 1
links = []

while i <= 4:
    page_url = "https://collection.artbma.org/objects/36930/3-men?ctx=ee9db81d7be350ec3d3fe6831b43ff897c65d199&idx=2"
    page = requests.get(page_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    primary_media_elements = soup.find_all('div', "primaryMedia img-wrap")
    
    for div_elem in primary_media_elements:
        link_elem = div_elem.find('a')
        #print(link_elem.attrs['href'])
        link = link_elem.attrs['href']
        links.append(link)

#print(len(links))

title = soup.find('h1').text
print(title)

 
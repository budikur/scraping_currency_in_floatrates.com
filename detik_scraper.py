"""
import requests
import bs4

url = 'https://www.detik.com/terpopuler?tag_from=framebar'
content = requests.get(url)
#print(content.text)
html = bs4.BeautifulSoup(content.text,"html.parser")
#print(html)
populer_area = html.find(attrs={'class': 'grid-row list-content'})
titles = populer_area.find_all(attrs={'class':'media__title'})
images = populer_area.find_all(attrs={'class':'media__image'})
#for t in titles:
for image in images:
    print(image.find('a').find('img')['title'])

#print(titles)
"""

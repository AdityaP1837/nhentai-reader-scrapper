url = "https://nhentai.to/?page=2"

import requests
from bs4 import BeautifulSoup

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

pagination = soup.find("section", class_="pagination").find_all("a")
for i in pagination:
    l = i["href"]
    info = {
                'link': l,
                'text': i.text
            }
    print(info)
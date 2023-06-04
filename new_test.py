url = "https://nhentai.to/tag/3d"

import requests
from bs4 import BeautifulSoup

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

all_tags_searched = soup.find_all("div", class_="gallery")

for tag in all_tags_searched:
    info = {
        "img": tag.a.img["data-src"],
        "title": tag.a.div.text,
        "link": tag.a["href"]
    }
    print(info)
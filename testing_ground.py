import requests
from bs4 import BeautifulSoup

url = "https://nhentai.to/tag/gender-morph"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

all_results = soup.find_all("div", class_="gallery")
tags_lists = []
for i in all_results:
            temp = i.a
            info = {
                "title": temp.div.text,
                "img": temp.img["data-src"],
                "page_link": i.a['href'],
            }
            tags_lists.append(info)

print(tags_lists)
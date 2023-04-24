import requests
from bs4 import BeautifulSoup

url = "https://nhentai.to/tags"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

#! Alphabetical Pagination
# atoz_pagination = [] 
# pagination = soup.find("ul", class_="alphabetical-pagination").find_all("li")

# for i in pagination:
#     atoz_pagination.append(url + (i.a["href"]))

#! Tags
tags_list = []
tags = soup.find() 
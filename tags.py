import requests
from bs4 import BeautifulSoup

url = "https://nhentai.to/tags"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

pages_limit = soup.findAll("a", class_="page")
pages_limit = int(pages_limit[-1].text)

all_pages_links = []
for i in range(pages_limit+1):
    if i == 0:
        pass
    else:
        link = f"{url}?page={i}"
        all_pages_links.append(link)

all_tags_data = []
for page_link in all_pages_links:
    i = requests.get(page_link).text
    s = BeautifulSoup(i, "html.parser")

    links = s.find_all("a", class_="tag")

    for link in links:
        info = {
            "a": link["href"],
            "text": (link.span.text).strip(),
            "count": link.find("span", class_="count").text
        }
        all_tags_data.append(info)
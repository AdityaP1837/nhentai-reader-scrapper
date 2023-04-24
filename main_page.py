import requests
from bs4 import BeautifulSoup

url = "https://nhentai.to/g/407576"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

#! Details
# details_list_img = soup.find("div", id="cover")

# details_list = soup.find("div", id="info")
# details_list_tags = (details_list.find("section", id="tags")).find_all(
#     "div", class_="tag-container"
# )
# tags_list = []
# artists_list = []

# tags = details_list_tags[0].find("span", class_="tags")
# artists = details_list_tags[1].find("span", class_="tags")

# for i in tags.find_all("a"):
#     data = {
#         "tag": i.find("span", class_="name").text,
#         "link": f'https://nhentai.to {i["href"]}',
#     }
#     tags_list.append(data)

# for i in artists.find_all("a"):
#     data = {
#         "tag": i.find("span", class_="name").text,
#         "link": f'https://nhentai.to {i["href"]}',
#     }
#     artists_list.append(data)

# info = {
#     "img": details_list_img.a.img["src"],
#     "title": details_list.h1.text,
#     "jp_title": details_list.h2.text,
#     "tags": tags_list,
#     "artists": artists_list,
#     "language": details_list_tags[-4].find("span", class_="name").text,
#     "categories": details_list_tags[-3].find("span", class_="name").text,
#     "pages": details_list_tags[-2].find("span", class_="name").text,
# }

#! Reading Page Images 
# images = soup.find("div", id="thumbnail-container").find_all(
#     "div", class_="thumb-container"
# )
# images_list = []
# for i in images:
#     link = i.a.img["data-src"]
#     images_list.append(link)

#! More Like This
# similar_contents = []
# similar = soup.find("div", class_="index-container").find_all("div", class_="gallery")
# for i in similar:
#     link = i.a
#     info = {
#         'link': link["href"],
#         'img': link.img["data-src"],
#         'title': i.find("div", class_="caption").text
#     }
#     similar_contents.append(info)
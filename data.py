import requests
from bs4 import BeautifulSoup

class Hanime_Brain:
    def __init__(self):
        self.url = "https://nhentai.to"
        self.response = requests.get(self.url)

    def main_page(self):
        soup = BeautifulSoup(self.response.content, "html.parser")
        all_container = soup.find_all("div", class_="index-container")

        #! Popular Now
        popular_container = all_container[0].find_all("div", class_="gallery")
        popular_lists = []
        for i in popular_container:
            temp = i.a
            info = {
                "title": temp.div.text,
                "img": temp.img["data-src"],
                "page_link": i.a['href'],
            }
            popular_lists.append(info)

        #! New Uploads
        new_uploads_container = all_container[1].find_all("div", class_="gallery")
        new_uploads_lists = []
        for i in new_uploads_container:
            temp = i.a
            info = {
                "title": temp.div.text,
                "img": temp.img["data-src"],
                "page_link": i.a['href']
            }
            new_uploads_lists.append(info)

        #! Pagination
        pagination_lists = []
        pagination = soup.find("section", class_="pagination").find_all("a")
        for i in pagination:
            l = str(i["href"])
            info = {
                'link': l.replace("https://nhentai.to/?", "/page/"),
                'text': i.text
            }
            pagination_lists.append(info)

        main_page_full_info = {
            'popular_now': popular_lists,
            'new_uploads': new_uploads_lists,
            'pagination': pagination_lists
        }
        return main_page_full_info
    
    def reading_page(self, id):
        url = f"{self.url}/g/{id}"
        r = requests.get(url)

        soup = BeautifulSoup(r.content, "html.parser")

        #! Details
        details_list_img = soup.find("div", id="cover")

        details_list = soup.find("div", id="info")
        details_list_tags = (details_list.find("section", id="tags")).find_all(
            "div", class_="tag-container"
        )
        tags_list = []
        artists_list = []

        tags = details_list_tags[0].find("span", class_="tags")
        artists = details_list_tags[1].find("span", class_="tags")

        for i in tags.find_all("a"):
            data = {
                "tag": i.find("span", class_="name").text,
                "link": i["href"]
            }
            tags_list.append(data)

        for i in artists.find_all("a"):
            data = {
                "artist": i.find("span", class_="name").text,
                "link": i["href"]
            }
            artists_list.append(data)

        manga_info = {
            "img": details_list_img.a.img["src"],
            "title": details_list.h1.text,
            "jp_title": details_list.h2.text,
            "tags": tags_list,
            "artists": artists_list,
            "language": details_list_tags[-4].find("span", class_="name").text,
            "categories": details_list_tags[-3].find("span", class_="name").text,
            "pages": details_list_tags[-2].find("span", class_="name").text,
        }

        #! Reading Page Images 
        images = soup.find("div", id="thumbnail-container").find_all(
            "div", class_="thumb-container"
        )
        images_list = []
        num = 1
        for i in images:
            link = i.a.img["data-src"].replace(f"{num}t", f"{num}")
            images_list.append(link)
            num += 1

        #! More Like This
        similar_contents = []
        similar = soup.find("div", class_="index-container").find_all("div", class_="gallery")
        for i in similar:
            link = i.a
            info = {
                'link': link["href"],
                'img': link.img["data-src"],
                'title': i.find("div", class_="caption").text
            }
            similar_contents.append(info)

        reading_page_info = {
            'manga_info': manga_info,
            'images': images_list,
            'similar': similar_contents
        }
        return reading_page_info
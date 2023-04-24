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
                "page_link": f"{self.url}{i.a['href']}",
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
                "page_link": f"{self.url}{i.a['href']}",
            }
            new_uploads_lists.append(info)

        #! Pagination
        pagination_lists = []
        pagination = soup.find("section", class_="pagination").find_all("a")
        pagination_lists.append(pagination)

        main_page_full_info = {
            'popular_now': popular_lists,
            'new_uploads': new_uploads_lists,
            'pagination': pagination_lists
        }
        return main_page_full_info
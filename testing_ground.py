import requests
from bs4 import BeautifulSoup

url = "https://nhentai.to/tags"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
ending_point = int(soup.find_all("a", class_="page")[-1].text)


# all_tags = ["num","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

sections_div = soup.find("div", class_="container").find_all("section")

for section in sections_div:
    info = {
        
    }

# for page in range(ending_point):
#     num = page + 1
#     print(num)
#     print("-------------------------")
#     url_page = url + "?page=" + str(num)
#     response = requests.get(url_page)
#     soup = BeautifulSoup(response.content, "html.parser")

#     sections_div = soup.find("div", class_="container").find_all("section")
#     print(sections_div)
#     print("\n")
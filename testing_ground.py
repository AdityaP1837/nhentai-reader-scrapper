import requests
from bs4 import BeautifulSoup

url = "https://nhentai.to/tags"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
ending_point = int(soup.find_all("a", class_="page")[-1].text)


# all_tags = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

sections_div = soup.find("div", class_="container").find_all("section")

# for section in sections_div:
#     for tag in section:
#         tag.h2.text
#         info = 
#         print()
#         print("\n")

for i in sections_div:
    print(i["id"])
import requests
from bs4 import BeautifulSoup

link = "https://supercalorizator.ru/"
response = requests.get(link).text
#print(response)

soup = BeautifulSoup(response, 'lxml')
block = soup.find("body", style=None)
sub_block = block.find("div", id="tool")

#print(sub_block)
product_block = sub_block.find("div", id="calorizator_wrapper")
# print(product_block)
product_block2 = product_block.find("div", id="main_categories")

#print(product_block2)
product_block3 = product_block2.findAll("div", attrs={"class": "main_block"})

list_of_links = []
for i_block in product_block3:
    links = i_block.find_all("a")
    for i_link in links:
        href = i_link.get("href")
        list_of_links.append(href)

print(list_of_links)
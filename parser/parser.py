import requests
from bs4 import BeautifulSoup


def parsing_product(product_link: str):
    product_response = requests.get(product_link).text
    product_object = BeautifulSoup(product_response, 'lxml')
    block_body = product_object.find("body", style="padding-right: 0px;")
    block_tool = block_body.find("div", id="tool")
    block_wrapper = block_tool.find("div", id="calorizator_wrapper")
    block_product = block_wrapper.find("div", id="calorizator_products")
    block_wrapper2 = block_product.find("div", id="product_wrapper")
    block_links = block_wrapper2.find_all("a")
    list_of_links = []

    for i_block2 in block_links:
        links2 = i_block2.find_all("a")
        for i_link2 in links2:
            href2 = i_link2.get('href')
            list_of_links.append(product_link + href2)
    return list_of_links

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
        list_of_links.append(link + href)

print(list_of_links)

list_of_url = []
for i_url in list_of_links:





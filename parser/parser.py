# import requests
# from bs4 import BeautifulSoup
#
#
# def parsing_product(product_link: str):
#     product_response = requests.get(product_link).text
#     product_object = BeautifulSoup(product_response, 'lxml')
#     block_body = product_object.find("body", style=None)
#     block_tool = block_body.find("div", id="tool")
#     block_wrapper = block_tool.find("div", id="calorizator_wrapper")
#     block_product = block_wrapper.find("div", id="calorizator_products")
#     block_wrapper2 = block_product.find("div", id="products_wrapper")
#     block_product2 = block_wrapper2.find_all("div", class_="product")
#     list_of_href = []
#
#     for i in block_product2:
#         block_links = i.find_all("a")
#         for j in block_links:
#             if j.get("href").startswith("#"):
#                 list_of_href.append(j.get("href"))
#
#     list_of_full_links = []
#     for i_href in list_of_href:
#         list_of_full_links.append(product_link + i_href)
#     return list_of_full_links
#
#
# link = "https://supercalorizator.ru/"
# response = requests.get(link).text
# #print(response)
#
# soup = BeautifulSoup(response, 'lxml')
# block = soup.find("body", style=None)
# sub_block = block.find("div", id="tool")
#
# #print(sub_block)
# product_block = sub_block.find("div", id="calorizator_wrapper")
# # print(product_block)
# product_block2 = product_block.find("div", id="main_categories")
#
# #print(product_block2)
# product_block3 = product_block2.findAll("div", attrs={"class": "main_block"})
#
# list_of_links = []
# for i_block in product_block3:
#     links = i_block.find_all("a")
#     for i_link in links:
#         href = i_link.get("href")
#         list_of_links.append(link + href)
#
# print(list_of_links)
#
# list_of_url = []
# for i_url in list_of_links:
#     for j_url in parsing_product(i_url):
#         list_of_url.append(j_url)
#
# # print(list_of_url)
# print(parsing_product(list_of_links[0]))
import requests
from bs4 import BeautifulSoup


def get_product_links(base_url):
    response = requests.get(base_url).text
    soup = BeautifulSoup(response, 'lxml')
    product_blocks = soup.find("div", id="calorizator_wrapper").find_all("div", class_="main_block")
    return [base_url + link.find("a")["href"] for link in product_blocks]


def get_all_product_links(product_url):
    product_links = get_product_links(product_url)
    list_product_links = []
    for product_link in product_links:
        product_response = requests.get(product_link).text
        product_soup = BeautifulSoup(product_response, 'lxml')
        product_links_tags = product_soup.find_all("a", href=lambda href: href and href.startswith("#"))
        product_links_urls = [product_link + tag["href"] for tag in product_links_tags]
        list_product_links.extend(product_links_urls)
    return all_product_links


url = "https://supercalorizator.ru/"
all_product_links = get_all_product_links(url)
print(all_product_links)

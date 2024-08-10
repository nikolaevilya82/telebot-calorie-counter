# import time
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_product_links(base_url):
#     response = requests.get(base_url).text
#     soup = BeautifulSoup(response, 'lxml')
#     product_blocks = soup.find("div", id="calorizator_wrapper"
#                                ).find_all("div", class_="main_block")
#     return [base_url + link.find("a")["href"] for link in product_blocks]
#
#
# def get_all_product_links(product_url):
#     product_links = get_product_links(product_url)
#     list_product_links = []
#
#     for product_link in product_links:
#         product_response = requests.get(product_link).text
#         product_soup = BeautifulSoup(product_response, 'lxml')
#         product_links_tags = product_soup.find_all(
#             "a", href=lambda href: href and href.startswith("#m"))
#
#         product_links_urls = {product_link + tag["href"]
#                               for tag in product_links_tags}
#         list_product_links.extend(product_links_urls)
#
#     return list(list_product_links)
#
#
# def get_product_data(product_link: str):
#     response = requests.get(product_link).text
#     soup = BeautifulSoup(response, "lxml")
#     name_of_product = soup.find("div",
#                                 class_="pop_product_name").get_text(strip=True)
#     caloric = soup.find("span", class_="kkal").get_text(strip=True)
#     return name_of_product, caloric
#
#
# url = "https://supercalorizator.ru/"
# all_product_links = get_all_product_links(url)
# print(all_product_links)
# product_dict = {}
# for i_link in all_product_links[:10]:
#     product = get_product_data(i_link)
#     product_dict[product[0]] = product[1]
#     time.sleep(1)
#
# print(product_dict)
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
import time


@lru_cache(maxsize=128)
def get_product_links(base_url):
    response = requests.get(base_url).text
    soup = BeautifulSoup(response, 'lxml')
    product_blocks = soup.find("div", id="calorizator_wrapper").find_all("div", class_="main_block")
    return [base_url + link.find("a")["href"] for link in product_blocks]


def get_all_product_links(product_url):
    product_links = get_product_links(product_url)
    list_product_links = set()  # Используем множество вместо списка

    with ThreadPoolExecutor() as executor:
        results = [executor.submit(get_product_link_details, product_link) for product_link in product_links]
        for future in results:
            list_product_links.update(future.result())  # Добавляем результаты в множество

    return list(list_product_links)  # Преобразуем множество в список


@lru_cache(maxsize=128)
def get_product_link_details(product_link):
    product_response = requests.get(product_link).text
    product_soup = BeautifulSoup(product_response, 'lxml')
    product_links_tags = product_soup.find_all("a", href=lambda href: href and href.startswith("#"))
    product_links_urls = [product_link + tag["href"] for tag in product_links_tags]
    return product_links_urls


def get_product_data(product_link: str):
    response = requests.get(product_link).text
    soup = BeautifulSoup(response, "lxml")
    name_of_product = soup.find("div", class_="pop_product_name").get_text(strip=True)
    caloric = soup.find("span", class_="kkal").get_text(strip=True)
    return name_of_product, caloric


url = "https://supercalorizator.ru/"
all_product_links = get_all_product_links(url)
product_dict = {}
for i_link in all_product_links[:6]:
    product = get_product_data(i_link)
    print(i_link)
    product_dict[product[0]] = product[1]
    time.sleep(1)

print(product_dict)

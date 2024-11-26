import time
from functools import lru_cache
from typing import Dict, List, Generator
import requests
from bs4 import BeautifulSoup
import logging


logger = logging.getLogger(__name__)

total_products = {}


@lru_cache(maxsize=128)
def get_product_links(base_url: str) -> Generator[str, None, None]:
    response = requests.get(base_url).text
    soup = BeautifulSoup(response, 'lxml')
    product_blocks = soup.find("div", id="calorizator_wrapper").find_all("div", class_="main_block")
    for link in product_blocks:
        yield base_url + link.find("a")["href"]


@lru_cache(maxsize=128)
def get_product(product_link: str) -> Dict[str, str]:
    product_response = requests.get(product_link).text
    product_soup = BeautifulSoup(product_response, 'lxml')
    products = product_soup.find_all("div", class_="product")
    product_dict = {}

    for i_product in products:
        product_name = i_product.find("div", class_='product_name').get_text(strip=True)
        product_calorie = i_product.find("span", class_="kkal_visible").get_text(strip=True)
        product_dict[product_name] = product_calorie
    print(product_dict)

    return product_dict


def get_all_product_data(base_url: str) -> Dict[str, str]:
    list_of_links: List[str] = list(get_product_links(base_url))
    global total_products
    total_products = {}
    for i_link in list_of_links[:2]:
        total_products.update(get_product(i_link))
        time.sleep(1)
    if len(total_products) > 0:
        logger.info("Парсинг продуктов завершён.")
    else:
        logger.warning("Не удалось получить продукты.")
    return total_products


# if __name__ == '__main__':
#     get_all_product_data("https://supercalorizator.ru")
#     get_product("https://supercalorizator.ru")
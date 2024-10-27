import re
from database.common.models import db, BaseModel
from database.utils.CRUD import store_data


def create_pattern(word) -> str:
    patterns = []
    for i in range(len(word)):
        patterns.append(word[:i] + '.' + word[i + 1:])

    for i in range(len(word)):
        patterns.append(word[:i] + word[i + 1:])
    final_pattern = '|'.join(patterns)
    print(final_pattern)
    return final_pattern


def product_search(product_name: str, product_dict) -> str:

    if product_name not in product_dict.keys:
        pattern = create_pattern(product_name)
        for i_name in product_dict.keys:
            if i_name == re.match(pattern, i_name):
                product_name = i_name
                return product_name

    else:
        return product_dict[product_name]


def add_calorie(data_base: db, user, calorie):
    store_data(data_base, user, calorie)




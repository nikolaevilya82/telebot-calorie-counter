import re
import logging
from database.common.models import db, BaseModel
from database.utils.CRUD import store_data
from calculation.formulas import calorie_calculation_product


logger = logging.getLogger(__name__)


def create_pattern(word: str) -> str:
    """создаем шаблоны, заменяя каждую букву на точку и удаляя каждую букву."""
    patterns = ([word[:i] + '.' + word[i + 1:] for i in range(len(word))] +
                [word[:i] + word[i + 1:] for i in range(len(word))])
    print(patterns)
    return '|'.join(patterns)


def product_search(product_name: str, product_weight: float, product_dict: dict) -> str:
    """Поиск среди всех ключей с использованием фильтрации по регулярному выражению
    и вычисление количества калорий, соответствующих весу продукта."""
    print('product dict', product_dict)
    calorie_in_100 = product_dict.get(product_name)
    print('calorie_in_100', calorie_in_100)

    if calorie_in_100 is None:
        pattern = create_pattern(product_name)

        for i_name in product_dict.keys():
            if re.fullmatch(pattern, i_name):
                calorie_in_100 = product_dict[i_name]
                break

    if calorie_in_100:
        print('calorie_in_100', calorie_in_100)
        return calorie_calculation_product(product_weight, calorie_in_100)
    else:
        logger.info('Продукта, который ввёл пользователь, '
                    'не оказалось в словаре парсинга продуктов.')
        return 'Такой продукт не найден.'


# def add_calorie(data_base: db, user, calorie, user_tg_id):
#     """Добавляет калории к уже съеденному сегодня и проверяет не превышена ли суточная норма."""
#     user_daily_norm = user.select(user.daily_norm).where(user.tg_id == user_tg_id)
#     user_calorie_now = user.select(user.calories_now).where(user.tg_id == user_tg_id)
#     new_calorie = user.calories_now + int(calorie)
#     user.update(calories_now=new_calorie).where(user.tg_id == user_tg_id).execute()
#     if new_calorie > user_daily_norm:
#         return "Суточная норма превышена"
def add_calorie(data_base: db, user, calorie, user_tg_id):
    """Добавляет калории к уже съеденному сегодня и проверяет не превышена ли суточная норма."""

    user_entry = user.get(user.tg_id == user_tg_id)
    user_daily_norm = user_entry.daily_norm
    user_calorie_now = user_entry.calories_now
    new_calorie = user_calorie_now + int(calorie)
    user.update(calories_now=new_calorie).where(user.tg_id == user_tg_id).execute()

    if new_calorie > user_daily_norm:
        return "Суточная норма превышена"


if __name__ == "__main__":
    create_pattern("udhgfu")
    products = {'abc': '234', 'dfg': '567'}
    eat = product_search('abg', 300, products)
    print(eat)


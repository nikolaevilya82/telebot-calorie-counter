import re
from database.common.models import db, BaseModel
from database.utils.CRUD import store_data
from calculation.formulas import calorie_calculation_product


def create_pattern(word: str) -> str:
    """создаем шаблоны, заменяя каждую букву на точку и удаляя каждую букву."""
    patterns = ([word[:i] + '.' + word[i + 1:] for i in range(len(word))] +
                [word[:i] + word[i + 1:] for i in range(len(word))])
    print(patterns)
    return '|'.join(patterns)


def product_search(product_name: str, product_weight: float, product_dict: dict) -> str:
    """Поиск среди всех ключей с использованием фильтрации по регулярному выражению
    и вычисление количества калорий, соответствующих весу продукта."""
    calorie_in_100 = product_dict.get(product_name)

    if calorie_in_100 is None:
        pattern = create_pattern(product_name)

        for i_name in product_dict.keys():
            if re.fullmatch(pattern, i_name):
                calorie_in_100 = product_dict[i_name]
                break

    if calorie_in_100:
        return calorie_calculation_product(product_weight, calorie_in_100)
    else:
        return 'Такой продукт не найден.'


def add_calorie(data_base: db, user, calorie, user_tg_id):
    """Добавляет калории к уже съеденному сегодня и проверяет не превышена ли суточная норма."""
    user_daily_norm = user.select(user.daily_norm).where(user.tg_id == user_tg_id)
    user_calorie_now = user.select(user.calories_now).where(user.tg_id == user_tg_id)
    data_base.update(user.calories_now + calorie)
    if user_calorie_now + int(calorie) > user_daily_norm:
        return "Суточная норма превышена"


if __name__ == "__main__":
    create_pattern("udhgfu")


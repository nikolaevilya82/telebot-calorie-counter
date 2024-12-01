from keyboards.inline import inline_buttons
from database.utils.CRUD import store_data
from database.common.models import User, db
from states.user_information import UserInfoState
from states.user_information import UserInfoState
from keyboards.inline import inline_buttons
from calculation.user_counter_now import product_search, add_calorie


def add_user_calories(bot, products):

    product_parameters = {}

    @bot.message_handler(func=lambda message: message.text == "Добавить продукт.")
    def get_product(message):
        bot.send_message(chat_id=message.chat.id,
                         text="Введите продукт или блюдо, которое Вы сегодня сьели.")
        bot.set_state(message.from_user.id, UserInfoState.product)

    @bot.message_handler(state=UserInfoState.product)
    def get_product_weight(message):
        product_parameters["product_now"] = message.text.lower()
        bot.send_message(chat_id=message.chat.id,
                         text="Введите вес продуктa или блюда в граммах.")
        bot.set_state(message.from_user.id, UserInfoState.product_weight)

    @bot.message_handler(state=UserInfoState.product_weight)
    def add_calories(message):
        product_parameters["product_weight"] = message.text
        print(product_parameters)
        eaten_food = product_search(product_parameters['product_now'],
                                    product_parameters["product_weight"],
                                    products)
        calories_gained = add_calorie(data_base=db, user=User, calorie=eaten_food,
                                      user_tg_id=message.from_user.id)
        if calories_gained == 'Суточная норма превышена':
            bot.send_message(chat_id=message.chat.id,
                             text="Суточная норма калорий превышена")






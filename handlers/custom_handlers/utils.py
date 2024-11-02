from keyboards.inline import inline_buttons
from database.utils.CRUD import store_data
from database.common.models import User, db
from states.user_information import UserInfoState
from states.user_information import UserInfoState
from keyboards.inline import inline_buttons


def add_user_calories(bot):

    product_parameters = {}

    @bot.message_handler(func=lambda message: message.text == "Добавить продукт.")
    def get_product(message):
        """"""
        # TODO Удалить клавиатуру.
        bot.send_message(chat_id=message.chat.id,
                         text="Введите продукт или блюдо, которое Вы сегодня сьели.")
        bot.set_state(message.from_user.id, UserInfoState.product)

    @bot.message_handler(state=UserInfoState.product)
    def get_product_weight(message):
        product_parameters["product_now"] = message.text
        bot.send_message(chat_id=message.chat.id,
                         text="Введите вес продуктa или блюда в граммах.")
        bot.set_state(message.from_user.id, UserInfoState.product_weight)

    @bot.message_handler(state=UserInfoState.product_weight)
    def add_calories(message):
        product_parameters["product_name"] = message.text
        print(product_parameters)
        store_data(db, User, User.calories_now, calorie_count)





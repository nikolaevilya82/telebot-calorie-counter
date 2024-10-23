from keyboards.inline import inline_bottons
from database.utils.CRUD import store_data
from database.common.models import User, db
from states.user_information import UserInfoState
from states.user_information import UserInfoState


product_parameters = {}


def add_user_calories(bot):
    product_parameters = {}
    global product_parameters

    @bot.message_handler(state=UserInfoState.gender,
                         func=lambda callback_query: callback_query.data == "product")
    def get_product(callback_query):
        """"""
        # TODO Удалить клавиатуру.
        bot.send_message(chat_id=callback_query.message.chat.id,
                         text="Введите продукт или блюдо, которое Вы сегодня сьели.")
        bot.set_state(callback_query.from_user.id, UserInfoState.product)

    @bot.message_handler(state=UserInfoState.product)
    def get_product_weight(message):
        product_parameters["product_now"] = message.data
        bot.send_message(chat_id=message.chat.id,
                         text="Введите продуктa или блюда в граммах.")
        bot.set_state(message.from_user.id, UserInfoState.product_weight)

    @bot.message_handler(state=UserInfoState.product_weight)
    def add_calories(message):
        product_parameters["product_name"] = message.data





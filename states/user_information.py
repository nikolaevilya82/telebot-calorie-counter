from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):
    calorie_now = State()
    gender = State()
    age = State()
    weight = State()
    user_height = State()
    ready = State()
    product = State()
    product_weight = State()

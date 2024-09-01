from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telebot import TeleBot


def gen_markup():
    # Создаём объекты кнопок.
    button_1 = KeyboardButton(text="Пройти опрос.")
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_1)
    return keyboard
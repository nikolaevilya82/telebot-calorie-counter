from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telebot import TeleBot


def gen_survey():
    # Создаём объекты кнопок.
    button_1 = KeyboardButton(text="Пройти опрос.")
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_1)
    return keyboard


def ate_now():
    button_1 = KeyboardButton(text="Добавить продукт.")
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_1)
    return keyboard

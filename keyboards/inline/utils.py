from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import TeleBot


def is_gender():
    # Создаём объекты кнопок.
    button_1 = InlineKeyboardButton(text="Ваш пол?", callback_data="dog")
    button_2 = InlineKeyboardButton(text="Ваш вес (в кг)?", callback_data="cat")
    button_2 = InlineKeyboardButton(text="Ваш рост (в см)?", callback_data="cat")
    button_2 = InlineKeyboardButton(text="Ваш возраст?", callback_data="cat")


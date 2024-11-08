from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import TeleBot


def is_gender():
    """Кнопки выбора пола пользователя."""
    button_1 = InlineKeyboardButton(text="Мужской", callback_data="man")
    button_2 = InlineKeyboardButton(text="Женский", callback_data="woman")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button_1, button_2)
    return keyboard


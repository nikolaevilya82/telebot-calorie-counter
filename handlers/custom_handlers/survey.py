import os
from dotenv import load_dotenv
import telebot
from keyboards.inline import utils

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
survey_parameters = {}


def take_survey(chat_id):
    bot.send_message(chat_id, "Выберите Ваш пол.",
                     reply_markup=utils.is_gender())


@bot.callback_query_handler(func=lambda callback_query: callback_query.data in ["man", "woman"])
def add_gender(callback_query):
    # Сохраняем пол в глобальной переменной
    survey_parameters["gender"] = callback_query.text
    print(survey_parameters)


if __name__ == "__main__":
    bot.infinity_polling()
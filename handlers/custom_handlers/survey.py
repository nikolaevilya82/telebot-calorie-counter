import os
from dotenv import load_dotenv
import telebot
from keyboards.inline import utils

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
survey_parameters = tuple()


def take_survey(chat_id):
    bot.send_message(chat_id,"Выберите Ваш пол.",
                     reply_markup=utils.is_gender())


@bot.message_handler(func=lambda message: message.text == "man")
def add_gender():
    return ("man",)


if __name__ == "__main__":
    bot.infinity_polling()
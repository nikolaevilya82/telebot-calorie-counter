import os
from dotenv import load_dotenv
import telebot
from keyboards.inline import utils

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


def take_survey(chat_id):
    bot.send_message(chat_id,"Выберите Ваш пол.",
                     reply_markup=utils.is_gender())



if __name__ == "__main__":
    bot.infinity_polling()
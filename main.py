import os
import time
from dotenv import load_dotenv
import telebot
from handlers.default_handlers import start
from handlers.default_handlers.survey import survey_parameters
from database.common import models


def create_first_table(date_base, user):
    with date_base:
        date_base.create_tables([user])
    # core.add_user(user, survey_param)


create_first_table(models.db, models.User)

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

start.new_user_start(bot)


if __name__ == '__main__':
    bot.infinity_polling()

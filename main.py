import os
import time
import schedule
from dotenv import load_dotenv
import telebot
from telebot.custom_filters import StateFilter
from handlers.default_handlers import start
from database.common import models
from api.parser import get_all_product_data
from handlers.custom_handlers.utils import add_user_calories
from states.user_information import UserInfoState


def create_first_table(date_base, user):
    with date_base:
        date_base.create_tables([user])


schedule.every().day.at(13.50).do(get_all_product_data("https://supercalorizator.ru"))
create_first_table(models.db, models.User)

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

start.new_user_start(bot)
if UserInfoState.ready:
    add_user_calories(bot)

if __name__ == '__main__':
    bot.add_custom_filter(StateFilter(bot))
    bot.infinity_polling()

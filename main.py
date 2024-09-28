import os
from dotenv import load_dotenv
import telebot
from handlers.default_handlers import start
load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
start.new_user_start(bot)


if __name__ == '__main__':
    bot.infinity_polling()

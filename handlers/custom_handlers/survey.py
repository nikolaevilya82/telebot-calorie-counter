import os
from dotenv import load_dotenv
import telebot


load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


if __name__ == "__main__":
    bot.infinity_polling()
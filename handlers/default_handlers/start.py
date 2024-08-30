import os
from dotenv import load_dotenv
import telebot
from keyboards.reply import utils

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.from_user.id, f"Здравствуйте{"""name"""}"
                              f"!Это бот, который считает калории съеденных Вами продуктов за день. "
                              f"Для того, что бы рассчитать Вашу суточную норму калорий пройдите опрос",
                     reply_markup=utils.gen_markup())


if __name__ == '__main__':
    bot.infinity_polling()
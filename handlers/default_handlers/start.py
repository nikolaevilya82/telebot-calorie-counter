import os
from dotenv import load_dotenv
import telebot
from telebot.types import ReplyKeyboardRemove
from keyboards.reply import utils
from handlers.custom_handlers import survey

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                f"Здравствуйте{"""name"""}"
                     f"!Это бот, который считает калории съеденных Вами продуктов за день. "
                     f"Для того, что бы рассчитать Вашу суточную норму калорий пройдите опрос",
                     reply_markup=utils.gen_markup())


@bot.message_handler(func=lambda message: message.text == "Пройти опрос.")
def get_survey(message):
    survey.take_survey(message.chat.id)
    bot.send_message(
        message.from_user.id,
         f"Ваша суточная норма калорий {"""calories"""}",
        reply_markup=ReplyKeyboardRemove())


if __name__ == '__main__':
    bot.infinity_polling()
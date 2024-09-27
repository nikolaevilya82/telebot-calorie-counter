import os
from dotenv import load_dotenv
import telebot
from keyboards.reply import reply_bottons
from handlers.default_handlers import survey
load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    print(message)
    bot.send_message(message.from_user.id,
                f"Здравствуйте {message.chat.first_name}! "
                     f"Это бот, который считает калории съеденных Вами продуктов за день. "
                     f"Для того, что бы рассчитать Вашу суточную норму калорий пройдите опрос",
                     reply_markup=reply_bottons.gen_markup())

    if message:
        survey.get_surv(bot)


if __name__ == '__main__':
    bot.infinity_polling()
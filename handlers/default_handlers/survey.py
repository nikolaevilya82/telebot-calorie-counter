import os
from dotenv import load_dotenv
import telebot
from keyboards.inline import inline_bottons


# load_dotenv()
# TOKEN = os.getenv('BOT_TOKEN')
# bot = telebot.TeleBot(TOKEN)
survey_parameters = {}


def get_surv(TOKEN, bot):
    print('get_surv started')

    @bot.message_handler(func=lambda message: message.text == "Пройти опрос.")
    def take_survey(message):
        bot.reply_to(message, "Выберите Ваш пол.",
                     reply_markup=inline_bottons.is_gender())


    @bot.callback_query_handler(func=lambda callback_query: callback_query.data in ["man", "woman"])
    def add_gender(callback_query):
        # Сохраняем пол в глобальной переменной
        survey_parameters["gender"] = callback_query.data
        print(survey_parameters)


    @bot.message_handler(func=lambda message: True)
    def is_age(chat_id):
        bot.send_message(chat_id, "Введите Ваш возраст.")





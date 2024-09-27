from keyboards.inline import inline_bottons


survey_parameters = {}


def get_surv(bot):
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
        bot.send_message(chat_id=callback_query.message.chat.id, text="Введите Ваш возраст.")

    @bot.message_handler(func=lambda message: 'age' not in survey_parameters
                         and 'gender' in survey_parameters)
    def add_age(message):
        survey_parameters['age'] = message.text
        print(survey_parameters)
        bot.send_message(message.chat.id, text="Введите Ваш вес в килограммах.")

    @bot.message_handler(func=lambda message: 'age' in survey_parameters
                         and 'gender' in survey_parameters and 'weight' not in survey_parameters)
    def add_weight(message):
        survey_parameters['weight'] = message.text
        print(survey_parameters)
        bot.send_message(message.chat.id, text="Введите Ваш рост в сантиметрах.")

    @bot.message_handler(func=lambda message: 'age' in survey_parameters
                         and 'gender' in survey_parameters and 'weight' in survey_parameters
                         and 'height' not in survey_parameters)
    def add_height(message):
        survey_parameters['height'] = message.text
        print(survey_parameters)
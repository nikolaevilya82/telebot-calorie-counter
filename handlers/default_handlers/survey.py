from keyboards.inline import inline_bottons
from calculation import formulas


survey_parameters = {}


def get_surv(bot):
    global survey_parameters
    survey_parameters = {}

    @bot.message_handler(func=lambda message: message.text == "Пройти опрос.")
    def is_gender(message):
        """Начало опроса пользователя."""
        bot.reply_to(message, "Выберите Ваш пол.",
                     reply_markup=inline_bottons.is_gender())

    @bot.callback_query_handler(func=lambda callback_query: callback_query.data in ["man", "woman"])
    def add_gender(callback_query):
        """Добавляет пол пользователя в глобальную переменную survey_parametres
         и запрашивает возраст пользователя"""
        survey_parameters["gender"] = callback_query.data
        print(survey_parameters)
        bot.send_message(chat_id=callback_query.message.chat.id, text="Введите Ваш возраст.")

    @bot.message_handler(func=lambda message: 'age' not in survey_parameters
                         and 'gender' in survey_parameters)
    def add_age(message):
        """Добавляет возраст пользователя в глобальную переменную survey_parametres
         и запрашивает вес пользователя"""
        survey_parameters['age'] = message.text
        print(survey_parameters)
        bot.send_message(message.chat.id, text="Введите Ваш вес в килограммах.")

    @bot.message_handler(func=lambda message: 'age' in survey_parameters
                         and 'gender' in survey_parameters and 'weight' not in survey_parameters)
    def add_weight(message):
        """Добавляет возраст пользователя в глобальную переменную survey_parametres
                 и запрашивает рост пользователя"""
        survey_parameters['weight'] = message.text
        print(survey_parameters)
        bot.send_message(message.chat.id, text="Введите Ваш рост в сантиметрах.")

    @bot.message_handler(func=lambda message: 'age' in survey_parameters
                         and 'gender' in survey_parameters and 'weight' in survey_parameters
                         and 'height' not in survey_parameters)
    def add_height(message):
        """Добавляет рост пользователя в глобальную переменную survey_parametres,
           запрашивает вес пользователя и выводит в чат суточную норму калорий пользователя."""
        survey_parameters['height'] = message.text
        survey_parameters['user_id'] = message.chat.id
        survey_parameters['user_name'] = message.chat.first_name
        print(survey_parameters)
        bot.send_message(message.chat.id, text=f"Ваша суточная норма калорий: {survey_result()}.")
    return survey_parameters


def survey_result() -> str:
    if survey_parameters['gender'] == 'man':
        return formulas.calorie_calculation_men(weight=survey_parameters['weight'],
                                                height=survey_parameters['height'],
                                                age=survey_parameters['age'])
    else:
        return formulas.calorie_calculation_women(weight=survey_parameters['weight'],
                                                height=survey_parameters['height'],
                                                age=survey_parameters['age'])


survey_parameters['daily_norm'] = survey_result()

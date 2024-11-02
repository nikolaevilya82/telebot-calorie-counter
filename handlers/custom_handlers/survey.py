from keyboards.reply import reply_bottons
from keyboards.inline import inline_buttons
from calculation import formulas
from database.utils.CRUD import store_user
from database.common.models import User, db
from states.user_information import UserInfoState
from handlers.custom_handlers.utils import add_user_calories


survey_parameters = {}


def get_surv(bot) -> None:
    global survey_parameters
    survey_parameters = {}

    @bot.message_handler(func=lambda message: message.text == "Пройти опрос.")
    def is_gender(message):
        """Начало опроса пользователя."""
        bot.reply_to(message, "Выберите Ваш пол.",
                     reply_markup=inline_buttons.is_gender())

    @bot.callback_query_handler(func=lambda callback_query: callback_query.data in ["man", "woman"])
    def add_gender(callback_query):
        """Добавляет пол пользователя в глобальную переменную survey_parameters
         и запрашивает возраст пользователя"""
        survey_parameters["user_gender"] = callback_query.data
        bot.set_state(callback_query.from_user.id, UserInfoState.gender)
        print(survey_parameters)
        bot.send_message(chat_id=callback_query.message.chat.id, text="Введите Ваш возраст.")

    @bot.message_handler(state=UserInfoState.gender)
    def add_age(message):
        """Добавляет возраст пользователя в глобальную переменную survey_parameters
         и запрашивает вес пользователя"""
        survey_parameters['user_age'] = message.text
        bot.set_state(message.from_user.id, UserInfoState.age)
        print(survey_parameters)
        bot.send_message(message.chat.id, text="Введите Ваш вес в килограммах.")

    @bot.message_handler(state=UserInfoState.age)
    def add_weight(message):
        """Добавляет возраст пользователя в глобальную переменную survey_parameters
                 и запрашивает вес пользователя"""
        survey_parameters['user_weight'] = message.text
        bot.set_state(message.from_user.id, UserInfoState.weight)
        print(survey_parameters)
        bot.send_message(message.chat.id, text="Введите Ваш рост в сантиметрах.")

    @bot.message_handler(state=UserInfoState.weight)
    def add_height(message):
        """Добавляет рост, id, имя и суточную норму калорий пользователя
           в глобальную переменную survey_parameters,"""
        survey_parameters['user_height'] = message.text
        survey_parameters['tg_id'] = message.chat.id
        survey_parameters['user_name'] = message.chat.first_name
        survey_parameters['daily_norm'] = survey_result()
        print(survey_parameters)

        store_user(db, User, message.chat.id, survey_parameters)
        bot.set_state(message.from_user.id, UserInfoState.ready)
        bot.send_message(message.chat.id, text=f"Ваша суточная норма калорий: {survey_result()}.")
        bot.send_message(message.from_user.id,
                         text="Что бы начать считать калории, нажмите <Добавить калории> внизу.",
                         reply_markup=reply_bottons.ate_now())
        add_user_calories(bot)


def survey_result() -> str:
    """Рассчитывает ежедневную норму калорий пользователя."""
    if survey_parameters['user_gender'] == 'man':
        return formulas.calorie_calculation_men(weight=survey_parameters['user_weight'],
                                                height=survey_parameters['user_height'],
                                                age=survey_parameters['user_age'])
    else:
        return formulas.calorie_calculation_women(weight=survey_parameters['user_weight'],
                                                height=survey_parameters['user_height'],
                                                age=survey_parameters['user_age'])

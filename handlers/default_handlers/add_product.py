from keyboards.reply import reply_bottons
from states.user_information import UserInfoState


def new_product(bot):
    @bot.message_handler(state=UserInfoState.ready)
    def send_welcome(message):
        bot.send_message(message.from_user.id, "Чтобы рассчитать сколько вы сегодня съели калорий"
                         "нажмите Добавить продукт.", reply_markup=reply_bottons.ate_now())


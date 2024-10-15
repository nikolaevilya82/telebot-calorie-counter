from keyboards.reply import reply_bottons
from handlers.custom_handlers import survey


def new_user_start(bot):
    @bot.message_handler(commands=["start"])
    def send_welcome(message):
        bot.send_message(message.from_user.id,
                    f"Здравствуйте {message.chat.first_name}! "
                         f"Это бот, который считает калории съеденных Вами продуктов за день. "
                         f"Для того, что бы рассчитать Вашу суточную норму калорий пройдите опрос",
                         reply_markup=reply_bottons.gen_markup())

        if message:
            survey.get_surv(bot)



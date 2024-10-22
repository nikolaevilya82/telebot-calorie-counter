from keyboards.inline import inline_bottons
from database.utils.CRUD import store_data
from database.common.models import User, db
from states.user_information import UserInfoState

def add_user_calories(bot):
    @bot.message_handler(state=UserInfoState.gender)
    def add_calories(bot):


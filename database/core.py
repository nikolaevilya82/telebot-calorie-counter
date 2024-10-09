from typing import Dict, List, TypeVar
from database.common.models import BaseModel


T = TypeVar('T')
# db.create_tables([User])


def add_user(user, survey_param: Dict[str, str]):
    user(tg_id=int(survey_param['user_id']), user_name=survey_param['user_name'], user_gender=survey_param['gender'],
         user_age=int(survey_param['age']), user_weight=int(survey_param['weight']), user_height=int(survey_param['height']),
         daily_norm=int(survey_param['daily_norm'])).save()

# db.create_tables([User])
# User(tg_id=1, user_name='name', user_gender='gender', user_age=10, user_weight=20, user_height=30, daily_norm=50).save()




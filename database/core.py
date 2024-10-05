from database.common.models import User, db
from handlers.default_handlers.survey import survey_parameters


db.create_tables([User])
user = User(survey_parameters['user_id'], survey_parameters['name'], survey_parameters['gender'],
            survey_parameters['age'], survey_parameters['weight'], survey_parameters['height'],
            survey_parameters['daily_norm'])

db.create_tables([User])
User(tg_id=1, user_name='name', user_gender='gender', user_age=10, user_weight=20, user_height=30, daily_norm=50).save()




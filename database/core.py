from database.common.models import User
#from handlers.default_handlers.survey import survey_parameters


# user = User(survey_parameters['user_id'], survey_parameters['name'], survey_parameters['gender'],
#             survey_parameters['age'], survey_parameters['weight'], survey_parameters['height'],
#             survey_parameters['daily_norm'])
User(1, 'name', 'gender', 10, 20, 30, 50).save()




from database.common import models
from database.utils.CRUD import CRUDInterface
from handlers.default_handlers.survey import survey_parameters


models.db.create_tables([models.User])

user = models.User(survey_parameters['user_id'], survey_parameters['name'], survey_parameters['gender'],
                   survey_parameters['age'], survey_parameters['weight'], survey_parameters['height'],
                   survey_parameters['daily_norm'])
user.save()




from datetime import datetime
import peewee as pw
from typing import Optional

db = pw.SqliteDatabase('users_tgb.db')


class BaseModel(pw.Model):

    class Meta:
        database = db


class User(BaseModel):
    class Meta:
        db_table = 'Users'

    id: Optional[int]
    tg_id = pw.IntegerField()
    user_name = pw.CharField(max_length=150)
    user_gender = pw.CharField(max_length=150)
    user_age = pw.IntegerField()
    user_weight = pw.IntegerField()
    user_height = pw.IntegerField()
    daily_norm = pw.IntegerField()
    calories_now = pw.IntegerField(null=False, default=0)



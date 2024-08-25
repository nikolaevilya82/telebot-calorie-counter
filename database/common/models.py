from datetime import datetime
import peewee as pw


db = pw.SqliteDatabase('users_tgb')


class ModelBase(pw.Model):
    created_at = pw.DateField(default=datetime.now())

    class Meta:
        database = db


class User(ModelBase):
    number = pw.TextField
    message = pw.TextField


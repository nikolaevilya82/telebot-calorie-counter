from datetime import datetime
import peewee as pw


db = pw.SqliteDatabase('users_tgb.db')


class ModelBase(pw.Model):
    created_at = pw.DateField(default=datetime.now())

    class Meta:
        database = db


class User(ModelBase):
    tg_id = pw.IntegerField
    user_name = pw.TextField
    user_gender = pw.TextField
    user_age = pw.IntegerField
    user_weight = pw.IntegerField
    user_height = pw.IntegerField
    daily_norm = pw.IntegerField


if __name__ == '__main__':
    db.create_tables([User])
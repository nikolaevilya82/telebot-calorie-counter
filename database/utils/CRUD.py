from typing import Dict, List, TypeVar
from database.common.models import db, BaseModel
from peewee import ModelSelect

T = TypeVar('T')


def create_table(date_base: db, model: T) -> None:
    with date_base:
        date_base.create_tables([model])


def store_data(data_base: db, model: T, column, data) -> None:
    with data_base:
        model.column = data


def store_user(data_base: db, model: T, tg_id, data) -> None:
    if model.get_or_none(model.tg_id == tg_id):
        model.update(data).where(model.tg_id == tg_id).execute()
    else:
        with data_base.atomic():
            model.insert_many(data).execute()


def _retrieve_all_data(db: db, model: T, *columns: BaseModel) -> ModelSelect:
    with db.atomic():
        response = model.select(*columns)
    return response


def _delite_user(db: db, model: T, user_id) -> None:
    with db:
        model.delite().where(model.id == user_id)


# class CRUDInterface:
#     @staticmethod
#     def create():
#         return _store_date
#
#     @staticmethod
#     def retrieve():
#         return _retrieve_all_data
#
#     @staticmethod
#     def delite_user():
#         return _delite_user
#
#
# if __name__ == ":__main__":
#     _store_date()
#     _retrieve_all_data()
#     CRUDInterface()
from typing import Dict, List, TypeVar
from database.common.models import BaseModel
from peewee import ModelSelect
from database.common.models import db


T = TypeVar('T')


def _store_date(db: db, model: T, *data) -> None:
    with db.atomic():
        model.isert_many(*data).execute()


def _retrieve_all_data(db: db, model: T, *columns: BaseModel) -> ModelSelect:
    with db.atomic():
        response = model.select(*columns)
    return response


def _delite_user(db: db, model: T, user_id) -> None:
    with db:
        model.delite().where(model.id == user_id)


class CRUDInterface:
    @staticmethod
    def create():
        return _store_date

    @staticmethod
    def retrieve():
        return _retrieve_all_data

    @staticmethod
    def deite_user():
        return _delite_user


if __name__ == ":__main__":
    _store_date()
    _retrieve_all_data()
    CRUDInterface()
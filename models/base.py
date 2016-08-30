

from peewee import Model
from playhouse.sqlite_ext import SqliteExtDatabase


class Base(Model):
    class Meta:
        database = SqliteExtDatabase(None)



from peewee import CharField, IntegerField, BooleanField

from models.base import Base


class Character(Base):
    uuid = CharField()
    name = CharField()
    age = IntegerField(default=0)
    x = IntegerField(default=0)
    y = IntegerField(default=0)
    ai = BooleanField(default=True)



from peewee import CharField, IntegerField, BooleanField

from models.base import Base


class Character(Base):
    name = CharField()
    age = IntegerField(default=0)
    ai = BooleanField(default=True)

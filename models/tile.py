

from peewee import CharField, FloatField, IntegerField

from models.base import Base


class Tile(Base):
    uuid = CharField()
    x = IntegerField(default=0)
    y = IntegerField(default=0)
    altitude = IntegerField(default=0)
    ground_type = CharField(default='rock')

    character_uuid = CharField(default='')

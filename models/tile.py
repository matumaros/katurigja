

from peewee import FloatField, IntegerField

from models.base import Base


class Tile(Base):
    altitude = IntegerField(default=0)
    soil_percent = FloatField(default=0.0)

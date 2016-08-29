

from peewee import Model


class Base(Model):
    def __init__(self, db, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.database = db

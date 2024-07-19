from peewee import SqliteDatabase, Model, TextField, IntegerField

db = SqliteDatabase('database.db')


class Tickets(Model):
    user_id = IntegerField()

    class Meta:
        database = db


class Lottery(Model):
    winner = IntegerField(default=0)

    class Meta:
        database = db

from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

# * FUNCTION THAT CREATES THE DB AND ITS TABLES
def create_and_connect():
    db.connect()
    # *  db.create_tables([<lists_with_tables]>, safe=True) --> this allows to create tables without worrying about that the ones already exists
    db.create_tables([Person], safe=True)

# * EXECUTE THE CREATION OF THE DB
create_and_connect()
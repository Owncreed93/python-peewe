from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db

# * FUNCTION THAT CREATES THE DB AND ITS TABLES
def create_and_connect():
    db.connect()
    # *  db.create_tables([<lists_with_tables]>, safe=True) --> this allows to create tables without worrying about that the ones already exists
    db.create_tables([Person, Pet], safe=True)

def create_family_members():
    # * INSERT DATA METHOD ONE
    uncle_tommy = Person(name='Tommy', birthday=date(2000,11,11), is_relative=True)
    uncle_tommy.save()

    # * INSERT DATA METHOD TWO
    grandma_ana = Person.create(name="Ana", birthday=date(1960,10,10), is_relative=True)

    tommy_dog = Pet.create(owner=uncle_tommy, name="Fido", animal_type="Dog")
    grandma_anas_cat = Pet.create(owner=grandma_ana, name="Peluza", animal_type="Cat")

    tommy_dog.name = "Firulais"
    tommy_dog.save()

def create_family_pets():
    tommy_dog = Pet()

# * EXECUTE THE CREATION OF THE DB
create_and_connect()
create_family_members()
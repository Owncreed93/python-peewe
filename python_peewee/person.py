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
    grandma_rosa = Person.create(name="Rosa", birthday=date(1960,10,10), is_relative=True)

    tommys_dog = Pet.create(owner=uncle_tommy, name="Fido", animal_type="Dog")
    grandma_anas_cat = Pet.create(owner=grandma_ana, name="Peluza", animal_type="Cat")
    grandma_rosas_dog = Pet.create(owner=grandma_rosa, name="Firulais", animal_type="Dog")

    #tommys_dog.name = "Firulais"
    #tommys_dog.save()

def get_family_pets():
    print("*****************************************")
    for pet in Pet.select():
        print(f"Nombre: {pet.name}, Dueño: {pet.owner.name}, Raza: {pet.animal_type}")

def get_family_members():
    print("*****************************************")
    for person in Person.select():
        print(f"Nombre: {person.name}, Cumpleaños: {person.birthday}, Es familiar : {person.is_relative}")

def get_family_member_birthday(n):
    print("*******************************************")
    # * SEARCH METHOD 1
    # family_member = Person.select().where(Person.name == n).get()
    # * SEARCH METHOD 2
    family_member = Person.get(Person.name == n)
    print(f"El cumpleaños de {family_member.name} es en la fecha {family_member.birthday}")

def delete_person(per):
    query = Person.delete().where(Person.name == per)
    deleted_entries = query.execute()
    print(f"{deleted_entries} registros borrados.")

def delete_pet(n):
    query = Pet.delete().where(Pet.name == n)
    deleted_entries = query.execute()
    print(f"{deleted_entries} registros borrados.")

def delete_one_pet(n):
    query = Pet.delete().where(Pet.name == n)
    deleted_entry = query.delete_instance()
    print(f"{deleted_entry} registros borrado.")


# * EXECUTE THE CREATION OF THE DB
create_and_connect()
#create_family_members()
get_family_members()
get_family_pets()
#get_family_member_birthday('Tommy')
#delete_person("Tommy")
#delete_person("Ana")
#delete_pet("Firulais")
from input import *
from db.schemes import Film


def print_choose_entity():
    print("1 - film")
    print("2 - award")
    print("3 - producer")
def choose_command():
        return input("Choose command: \n")
def get_entity():
    while 1:
        print_choose_entity()
        i = choose_command()
        entities = {
            '1': 1,
            '2': 2,
            '3': 3
        }
        if i is 'q':
            break

        if i in entities:
            return entities[i]
        else:
            print("____________________")
            print("No such option, try again...")
def get_all(entity_type, db):
    entities = {
        1: db.get_films,
        2: db.get_awards,
        3: db.get_producers
    }

    if entity_type in entities:
        for entity in entities[entity_type]():
            print(entity)

def check_input(cb, helpstr, db=None):
    while True:
        try:
            if db is not None:
                return cb(helpstr, db)
            return cb(helpstr)
        except ValueError:
            print("Try again...")
            continue
def input_film(db):
    print("Input required values and press enter...")
    p = Film(title=input("Fullname: "),
             producer=input("Producer: "),
             date=check_input(input_date, "Date(dd-mm-yyyy): "),
             award_id=check_input(input_award_id, "Please input award id that exists or 0: ", db)
               )
    db.new_film(p)

def update_film(db):

    get_all(1,db)

    set_id = input("What id do you want UPDATE: \n")
    what_id = input("What new id: \n")
    # award =db.get_award_id(set_id)
    film = db.get_film_id(set_id)
    new_c = Film(film_id=what_id if what_id is not '' else film.film_id,
                  title=film.title, producer=film.producer, date=film.date, award_id =film.award_id)
    db.update_film(new_c)
    db.delete_film(set_id)


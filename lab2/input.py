from datetime import datetime


def input_award_id(str, db):
    id = int(input(str))
    if db.get_award_id(id) is not None:
        return id
    raise ValueError


def input_producer_id(str, db):
    id = int(input(str))
    if db.get_producer_id(id) is not None:
        return id
    raise ValueError


def input_film_id(str, db):
    id = int(input(str))
    if db.get_film_id(id) is not None:
        return id
    raise ValueError






def input_date(str):
    return datetime.strptime(input(str), '%d-%m-%Y')



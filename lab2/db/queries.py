from sqlalchemy.orm import sessionmaker
import sqlalchemy
from db.schemes import Film
from db.schemes import Award
from db.schemes import Producer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database:
    engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:080599@localhost/films')
    _Session = sessionmaker(bind=engine)

    def __init__(self):
        engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:080599@localhost/films')
        _Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)
        self.session = _Session()

    def get_films(self):
        rows = []
        for p in self.session.query(Film).\
                order_by(Film.film_id):
            rows.append(p)
        return rows

    def get_awards(self):
        rows = []
        for p in self.session.query(Award). \
                filter(Award.award_id > 0). \
                order_by(Award.award_id):
            rows.append(p)
        return rows

    def get_producers(self):
        rows = []
        for p in self.session.query(Producer). \
                filter(Producer.producer_id > 0). \
                order_by(Producer.producer_id):
            rows.append(p)
        return rows

    def get_film_id(self, id):
        return self.session.query(Film).get(id)

    def get_award_id(self, id):
        return self.session.query(Award).get(id)

    def get_producer_id(self, id):
        return self.session.query(Producer).get(id)

    def new_film(self, player):
        self.session.add(player)
        self.session.commit()

    def new_award(self, award):
        self.session.add(award)
        self.session.commit()

    def update_film(self, film):
        self.new_film(film)

    def delete_film(self, pid):
        self.session.delete(self.get_film_id(pid))
        self.session.commit()

    def delete_award(self, pid):
        self.session.delete(self.get_award_id(pid))
        self.session.commit()

    def search(self, text):
        if " " in text:
            text = text.replace(" ", " & ")

        sql = f"select * from film where to_tsvector(title) @@ plainto_tsquery('{text}') \
                    or to_tsvector(producer) @@ plainto_tsquery('{text}')"

        return self.engine.execute(sql).fetchall()

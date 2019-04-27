from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Film(Base):
    __tablename__ = 'film'

    film_id = Column(Integer, primary_key=True)

    title = Column(String)
    producer = Column(String)
    date = Column(Date)
    award_id = Column(Integer)

    def __repr__(self):
        return "<Film(# %2s| %15s | %10s | %10s | %s)>" %(str(self.film_id), self.title,  self.producer, str(self.date), str(self.award_id))


class Award(Base):
    __tablename__ = 'award'

    award_id = Column(Integer, primary_key=True)
    title = Column(String)
    def __repr__(self):
        return "<Award(# %3s | %8s )>" \
               % (str(self.award_id), self.title)


class Producer(Base):
    __tablename__ = 'producer'

    producer_id = Column(Integer, primary_key=True)

    name = Column(String)
    award_id = Column(Integer)

    def __repr__(self):
        return "<Agent(# %2s | %10s | %2s)>" \
               % (str(self.producer_id), self.name, str(self.award_id))

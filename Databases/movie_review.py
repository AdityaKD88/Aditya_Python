from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'Movie Review'
    id = Column(Integer, primary_key=True)
    movie_name = Column(String(20))
    director = Column(String(15))
    cast = Column(String(100))
    run_time = Column(Integer)
    review = Column(String)
    date = Column(DateTime, default=datetime.now())

def open_db():
    engine = create_engine('sqlite:///review.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session() 
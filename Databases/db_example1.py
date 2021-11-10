from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker
from datetime import datetime      # data and time related function

Base = declarative_base()       # special class dynamic generated by the function

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    section = Column(String(2))
    klass = Column(String(4))
    is_online = Column(Boolean, default=False)
    admit_date = Column(DateTime, default=datetime.now())

    def __str__(self):
        return f"{self.name} {self.klass}-{self.section}"

class Grade(Base):
    __tablename__ = 'student_grades'
    id = Column(Integer, primary_key=True)
    student = Column(ForeignKey('students.id'))
    hindi = Column(Integer)
    maths = Column(Integer)
    english = Column(Integer)
    total = Column(Integer)
    date = Column(DateTime, default=datetime.now())

    def __str__(self):
        return f"{self.total},{'Pass' if self.total>120 else 'Fail'}"


def open_db():
    engine = create_engine('sqlite:///student.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()    # this will give a connection to database


# open_db() - test run one time only
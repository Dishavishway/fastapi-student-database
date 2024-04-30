from sqlalchemy import String, Integer, Column, Boolean

from database import Base, engine


def create_tables():
    Base.metadata.create_all(engine)

class student(Base):
    __tablename__='Student'
    id = Column(Integer, primary_key=True)
    fname = Column(String(20), nullable=False)
    lname = Column(String(20), nullable=False)
    ismale = Column(Boolean)
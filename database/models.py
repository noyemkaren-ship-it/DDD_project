from sqlalchemy import Column, Integer, String

from database.db import Base


class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    balance = Column(Integer, default=0)

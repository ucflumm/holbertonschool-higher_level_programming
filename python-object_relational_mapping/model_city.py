#!/usr/bin/python3
"""
    a Python file similar to model_state.py named model_city.py that contains
    the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class City(Base):
    """
        Class definition of a City and an instance Base = declarative_base()
        inherits from Base
        links to the MySQL table cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
    state = relationship("State", back_populates="cities")

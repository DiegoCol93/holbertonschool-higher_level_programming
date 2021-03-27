#!/usr/bin/python3
''' Module for storing Base sub-class object definitions. '''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    '''
    City class, id(INT, auto, PRIMARY) and name(STRING(128), NOT NULL)
                state_id(INT, NOT NULL, FOREING KEY States.id)
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

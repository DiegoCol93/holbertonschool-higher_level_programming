#!/usr/bin/python3
''' Module for storing Base sub-class object definitions. '''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    ''' State class, id(INT, auto, PRIMARY) and name(STRING(128), NOT NULL)'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

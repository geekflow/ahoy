# -*- coding: utf-8 -*-
"""
    Function
    ~~~~~~~~~


    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from sqlalchemy import Column, Integer, String
from . import Base


class Function(Base):
    __tablename__ = 'gs_function'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<View %r %r>' % (self.id, self.name)

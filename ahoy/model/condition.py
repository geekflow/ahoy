# -*- coding: utf-8 -*-
"""
    Function
    ~~~~~~~~~


    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from sqlalchemy import Column, Integer, String
from . import Base


class Condition(Base):
    __tablename__ = 'gs_condition'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False)
    content = Column(String, unique=False)
    expect = Column(String, unique=False)
    actual = Column(String, unique=False)
    status = Column(Integer, unique=False)
    priority = Column(Integer, unique=False)
    note = Column(String, unique=False)

    def __init__(self, id, name, content, expect, actual, status, priority, note):
        self.id = id
        self.name = name
        self.content = content
        self.expect = expect
        self.actual = actual
        self.status = status
        self.priority = priority
        self.note = note

    def __repr__(self):
        return '<Condition %r %r %r %r %r %r %r %r>' % (
            self.id, self.name, self.content, self.expect, self.actual, self.status, self.priority, self.note)

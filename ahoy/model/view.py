# -*- coding: utf-8 -*-
"""
    Version
    ~~~~~~~~~


    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from sqlalchemy import Column, Integer, String
from . import Base


class Version(Base):
    __tablename__ = 'gs_view'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    parent_id = Column(Integer)
    depth = Column(Integer)
    sequence = Column(Integer)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<View %r %r %r %r %r>' % (self.id, self.name, self.parent_id, self.depth, self.sequence)

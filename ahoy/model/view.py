# -*- coding: utf-8 -*-
"""
    View
    ~~~~~~~~~


    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from sqlalchemy import Column, Integer, String

from . import Base


class View(Base):
    __tablename__ = 'gs_view'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    parent_id = Column(Integer)
    depth = Column(Integer)
    sequence = Column(Integer)

    def __init__(self, name, parent_id, depth, sequence):
        self.name = name
        self.parent_id = parent_id
        self.depth = depth
        self.sequence = sequence

    def __repr__(self):
        return '<View %r, %r, %r, %r, %r>' % (self.id, self.name, self.parent_id, self.depth, self.sequence)

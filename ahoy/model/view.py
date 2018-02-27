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
    parent_id = Column(Integer, nullable=False)
    depth = Column(Integer, nullable=False)
    sequence = Column(Integer, nullable=False)

    def __init__(self, name, parent_id, depth, sequence):
        self.name = name
        self.parent_id = parent_id
        self.depth = depth
        self.sequence = sequence

    def __eq__(self, other):
        return self.name == other.name and \
               self.parent_id == other.parent_id and \
               self.depth == other.depth and \
               self.sequence == other.sequence

    def __repr__(self):
        return '<View %r, %r, %r, %r, %r>' % (self.id, self.name, self.parent_id, self.depth, self.sequence)

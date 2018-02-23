# -*- coding: utf-8 -*-
"""
    Version
    ~~~~~~~~~


    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from sqlalchemy import Column, Integer, String

from . import Base


class Script(Base):
    __tablename__ = 'gs_script'

    id = Column(Integer, primary_key=True)
    content = Column(String, unique=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<Script %r %r %r %r %r>' % (self.id, self.name, self.parent_id, self.depth, self.sequence)

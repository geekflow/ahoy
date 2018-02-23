# -*- coding: utf-8 -*-
"""
    Version
    ~~~~~~~~~


    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from sqlalchemy import Column, Integer, String, DateTime
from . import Base


class Version(Base):
    __tablename__ = 'gs_version'

    id = Column(Integer, primary_key=True)
    version = Column(String(12), unique=True)
    start_date = Column(DateTime, unique=False)
    end_date = Column(DateTime, unique=False)

    def __init__(self, id, version, start_date, end_date):
        self.id = id
        self.version = version
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return '<Version %r %r %r %r>' % (self.id, self.version, self.start_date, self.end_date)

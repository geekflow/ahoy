# -*- coding: utf-8 -*-
"""
    RelatedViewFunction
    ~~~~~~~~~


    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from . import Base


class RelatedViewFunction(Base):
    __tablename__ = 'gs_related_view_function'

    version_id = Column(Integer, ForeignKey('gs_version.id'))
    view_id = Column(Integer, ForeignKey('gs_view.id'))
    function_id = Column(Integer, ForeignKey('gs_function.id'))

    def __init__(self, version_id, view_id, function_id):
        self.version_id = version_id
        self.view_id = view_id
        self.function_id = function_id

    def __repr__(self):
        return '<RelatedViewFunction %r %r %r>' % (self.version_id, self.view_id, self.function_id)

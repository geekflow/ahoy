# -*- coding: utf-8 -*-
"""
    RelatedFunctionCondition
    ~~~~~~~~~


    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from . import Base


class RelatedFunctionCondition(Base):
    __tablename__ = 'gs_related_function_condition'

    version_id = Column(Integer, ForeignKey('gs_version.id'))
    function_id = Column(Integer, ForeignKey('gs_function.id'))
    condition_id = Column(Integer, ForeignKey('gs_condition.id'))

    def __init__(self, version_id, function_id, condition_id):
        self.version_id = version_id
        self.function_id = function_id
        self.condition_id = condition_id

    def __repr__(self):
        return '<RelatedFunctionCondition %r %r %r>' % (self.version_id, self.function_id, self.condition_id)

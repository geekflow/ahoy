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


class RelatedConditionScript(Base):
    __tablename__ = 'gs_related_view_function'

    version_id = Column(Integer, ForeignKey('gs_version.id'))
    condition_id = Column(Integer, ForeignKey('gs_condition.id'))
    script_id = Column(Integer, ForeignKey('gs_script.id'))

    def __init__(self, version_id, condition_id, script_id):
        self.version_id = version_id
        self.condition_id = condition_id
        self.script_id = script_id

    def __repr__(self):
        return '<RelatedConditionScript %r %r %r>' % (self.version_id, self.condition_id, self.script_id)

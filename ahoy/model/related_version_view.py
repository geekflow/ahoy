# -*- coding: utf-8 -*-
"""
    RelatedVersionView
    ~~~~~~~~~


    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from . import Base


class RelatedVersionView(Base):
    __tablename__ = 'gs_related_version_view'

    version_id = Column(Integer, ForeignKey('gs_version.id'))
    view_id = Column(Integer, ForeignKey('gs_view.id'))

    view = relationship("View", backref=backref("views"))

    def __init__(self, version_id, view_id):
        self.version_id = version_id
        self.view_id = view_id

    def __repr__(self):
        return '<RelatedVersionView %r %r>' % (self.version_id, self.view_id)

# -*- coding: utf-8 -*-
"""
    RelatedVersionView
    ~~~~~~~~~


    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, backref
from . import Base


class RelatedVersionView(Base):
    __tablename__ = 'gs_related_version_view'
    __table_args__ = (
        PrimaryKeyConstraint('version_id', 'view_id'),
    )

    version_id = Column(Integer, ForeignKey('gs_version.id'), nullable=False)
    view_id = Column(Integer, ForeignKey('gs_view.id'), nullable=False)

    view = relationship("View", backref=backref("views"))

    def __init__(self, version_id, view_id):
        self.version_id = version_id
        self.view_id = view_id

    def __eq__(self, other):
        return self.version_id == other.version_id and self.view_id == other.view_id

    def __repr__(self):
        return '<RelatedVersionView %r %r>' % (self.version_id, self.view_id)

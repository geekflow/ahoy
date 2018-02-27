# -*- coding: utf-8 -*-
"""
    related_version_view
    ~~~~~~~~~

    .

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
import datetime

import pytest

from ahoy.model.related_version_view import RelatedVersionView
from ahoy.model.version import Version
from ahoy.model.view import View


@pytest.fixture(scope='function')
def setup(session):
    session.query(Version).delete()
    session.query(View).delete()

    version = Version('0.0.1', datetime.date.today(), datetime.date.today())
    session.add(version)

    view = View('DashBoard', 0, 1, 1)
    session.add(view)
    session.commit()


@pytest.mark.run(before='test_version')
def test_query_model(session, setup):
    version = session.query(Version).filter_by(version='0.0.1').first()
    view = session.query(View).filter_by(name='DashBoard').first()

    related_version_view = RelatedVersionView(version.id, view.id)
    session.add(related_version_view)
    session.commit()

    related_version_views = session.query(RelatedVersionView).filter_by(version_id=version.id, view_id=view.id).first()

    assert related_version_views == related_version_view

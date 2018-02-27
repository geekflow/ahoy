# -*- coding: utf-8 -*-
"""
    test_version
    ~~~~~~~~~

    .

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
import datetime

import pytest

from ahoy.model.version import Version


@pytest.fixture(scope='function')
def setup(session):
    session.query(Version).delete()

    version = Version('0.0.1', datetime.date.today(), datetime.date.today())
    session.add(version)
    session.commit()


def test_query_model(session):
    version = Version('0.0.1', datetime.date.today(), datetime.date.today())
    version.id = 1

    result = session.query(Version).all()

    assert len(result) == 1
    assert result == [version]

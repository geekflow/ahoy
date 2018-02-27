# -*- coding: utf-8 -*-
"""
    test_view
    ~~~~~~~~~

    .

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
import pytest

from ahoy.model.view import View


@pytest.fixture(scope='function')
def setup(session):
    session.query(View).delete()

    view = View('DashBoard', 0, 1, 1)
    session.add(view)
    session.commit()


def test_query_model(session, setup):
    view = View('DashBoard', 0, 1, 1)

    result = session.query(View).all()

    assert len(result) == 1
    assert result == [view]

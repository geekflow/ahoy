# -*- coding: utf-8 -*-
"""
    test_view
    ~~~~~~~~~

    .

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from ahoy.model.view import View


def test_query_model(session):
    # version = Version('0.0.1', datetime.date.today(), datetime.date.today())
    # session.add(version)
    # session.commit()

    view = View('DashBoard', 0, 1, 1)
    session.add(view)
    session.commit()

    result = session.query(View).all()

    assert len(result) == 1
    assert result == [view]

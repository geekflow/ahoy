# -*- coding: utf-8 -*-
"""
    test_ahoy
    ~~~~~~~~~

    ahoy init.

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
import os
import tempfile
import pytest
from ahoy.factory import create_app
from ahoy.blueprints.ahoy import init_db


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    print(db_path)
    config = {
        'DATABASE': db_path,
        'TESTING': True,
    }

    app = create_app(config=config)
    print(app.root_path)
    print(app.root_path)
    print(app.root_path)

    with app.app_context():
        init_db()
        yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


def test_empty_db(client):
    rv = client.get('/')
    assert b'Ahoy' in rv.data

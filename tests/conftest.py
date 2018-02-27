# -*- coding: utf-8 -*-
"""
    conftest
    ~~~~~~~~~


    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
import pytest
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
from flask import config, g
from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import sessionmaker

from ahoy.factory import create_app
from ahoy.model import Base
from ahoy.model.database import DBManager as _db

# TESTDB = 'test_ahoy.db'
# TESTDB_PATH = "/opt/project/data/{}".format(TESTDB)
# TEST_DATABASE_URI = 'sqlite:///' + TESTDB_PATH
from ahoy.model.version import Version
from ahoy.model.view import View

TEST_DATABASE_URI = 'sqlite:///:memory:'


# @pytest.fixture(scope='session')
# def app():
#     app = create_app()
#     app_context = app.app_context()
#     app_context.push()
#
#     yield app
#
#     app_context.pop()

@pytest.fixture(scope='session')
def app(request):
    settings_override = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': TEST_DATABASE_URI
    }

    app = create_app(config=settings_override)

    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)

    return app


@pytest.fixture(scope='session')
def flask_client(app):
    return app.test_client()


@pytest.fixture(scope='session')
def db(app, request):
    # if os.path.exists(TESTDB_PATH):
    #     os.unlink(TESTDB_PATH)
    #
    def teardown():
        Base.metadata.drop_all(_db.engine())
    #     os.unlink(TESTDB_PATH)

    _db.app = app
    # _db.engine().create_all()
    _db.init_db()

    request.addfinalizer(teardown)

    # return _db
    return _db.engine()

    # alembic_config = AlembicConfig(config['ALEMBIC_INI'])
    # alembic_config.set_main_option('sqlalchemy.url', config['TEST_DB_URL'])
    # alembic_upgrade(alembic_config, 'head')
    #
    # yield _db
    #
    # engine.dispose()


@pytest.fixture(scope='function')
def session(db, request):
    connection = db.engine.connect()
    transaction = connection.begin()

    # options = dict(bind=connection, binds={})
    # session = db.create_scoped_session(options=options)
    session = _db.session()

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)

    return session

# -*- coding: utf-8 -*-
"""
    factory
    ~~~~~~~~~

    ahoy init.

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

import os

from flask import Flask, request, url_for
from werkzeug.utils import find_modules, import_string

from ahoy.blueprints.ahoy import init_db


def print_settings(config):
    print('========================================================')
    print('SETTINGS for AHOY APPLICATION')
    print('========================================================')
    for key, value in config:
        print('%s=%s' % (key, value))
    print('========================================================')


def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)


def create_app(config_filepath='config/config.cfg', config=None):
    app = Flask(__name__, static_folder='static', static_url_path='', template_folder='templates')

    app.config.from_pyfile(config_filepath, silent=True)

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'ahoy.db'),
        DEBUG=True,
        SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
        USERNAME='admin',
        PASSWORD='admin',
        SITE_ROOT=os.path.abspath(os.path.dirname(__file__)),
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                            '../data/ahoy.db'),
        DB_LOG_FLAG='True'
    ))

    app.config.update(config or {})

    app.config.from_envvar('AHOY_SETTINGS', silent=True)
    app.config.from_object(__name__)

    from .model.database import DBManager as db
    db.init(app.config.get('SQLALCHEMY_DATABASE_URI'), eval(app.config['DB_LOG_FLAG']))
    db.init_db()

    register_blueprints(app)
    register_cli(app)

    init_db()

    app.jinja_env.globals['url_for_other_page'] = url_for_other_page

    return app


def register_blueprints(app):
    for name in find_modules('ahoy.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None


def register_cli(app):
    @app.cli.command('initdb')
    def init_db_command():
        """Creates the database tables."""
        init_db()
        print('Initialized the database.')

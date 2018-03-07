#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    .blueprint
    ~~~~~~~~~~~~~~~~~~

    blueprint module.

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from os.path import join

from flask import Blueprint, render_template
from flask import send_from_directory

bp = Blueprint('ahoy', __name__, template_folder='templates', static_folder='static')


def init_db():
    pass


@bp.record
def record(setup_state):
    global root_path
    app = setup_state.app
    root_path = app.root_path


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(join(root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

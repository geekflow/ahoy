#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    .blueprint
    ~~~~~~~~~~~~~~~~~~

    blueprint module.

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from flask import Blueprint, render_template

bp = Blueprint('ahoy', __name__, template_folder='templates', static_folder='static')


def init_db():
    pass


@bp.route('/')
def index():
    return render_template('index.html')

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    function
    ~~~~~~~~~~~~~~~~~~

    function module.

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from flask import session, redirect, request, url_for
from flask import render_template
from flask.views import MethodView

from ..blueprints.ahoy import bp
from ..decorator import template


class FunctionView(MethodView):

    # def dispatch_request(self):
    #     print('dispatch_request')
    #     return render_template('function/add.html', page=request.args['page'] or None)

    @template('function/add.html')
    def get(self):
        print('Function GET')
        return dict(page=request.args['page'] or None)

    def post(self):
        print('Function POST')
        pass

    def delete(self):
        print('Function DELETE')
        pass

    def put(self, page=None):
        print('Function put')
        pass


@bp.route('/ahoy/func', methods=['GET', 'POST'])
def add():
    print('call')
    return render_template('function/add.html')

# -*- coding: utf-8 -*-
"""
    .decorator
    ~~~~~~~~~

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from functools import wraps

from flask import render_template
from flask import request, session, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            is_login = False
            if 'user_info' in session:
                is_login = True
            if not is_login:
                return redirect(url_for('.login', next=request.url))
            return f(*args, **kwargs)
        except Exception as e:
            raise e

    return decorated_function


def user_required(f):
    def decorator(*args, **kwargs):
        print('user_required')
        return f(*args, **kwargs)

    return decorator


def template(name=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = name

            print(template_name)

            if template_name is None:
                template_name = request.endpoint.replace('.', '/') + '.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)

        return decorated_function

    return decorator

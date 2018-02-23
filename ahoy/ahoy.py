# -*- coding: utf-8 -*-
"""
    ahoy
    ~~~~~~~~~

    ahoy init.

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from ahoy.factory import create_app

app = create_app()


@app.route('/')
def hello_world():
    return 'Hello World!'


# -*- coding: utf-8 -*-
"""
    runserver
    ~~~~~~~~~

    use runserver local dev.

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from ahoy.factory import create_app

app = create_app()

if __name__ == '__main__':
    try:
        from os import environ

        if environ.get('WERKZEUG_RUN_MAIN') == 'true':
            print('################### Restarting @ {} ###################')

        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt as e:
        pass

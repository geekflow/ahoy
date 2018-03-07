#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    .controller.login
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from flask import request, session, redirect, url_for, flash
from flask import render_template
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms import Form, TextField, PasswordField, HiddenField, validators

from ..model.database import DBManager as db
from ..blueprints.ahoy import bp
from ..model.user import User
from ..decorator import login_required


@bp.teardown_request
def close_db_session(exception=None):
    try:
        db.session().remove()
    except Exception as e:
        # Log.error(str(e))
        raise e


@bp.route('/login', methods=['GET'])
def login_form():
    print('login_from')
    form = RegistrationForm(request.form)

    next_url = request.args.get('next', '')
    register_email = request.args.get('register_email', '')
    update_email = request.args.get('update_email', '')

    return render_template('login.html',
                           next_url=next_url,
                           form=form,
                           register_email=register_email,
                           update_email=update_email)


@bp.route('/login', methods=['POST'])
def login():
    form = RegistrationForm(request.form)

    login_error = None
    next_url = form.next_url.data

    if form.validate():

        if form.validate():
            session.permanent = True

            email = form.email.data
            password = form.password.data
            next_url = form.next_url.data

            # Log.info('(%s)next_url is %s' % (request.method, next_url))

            try:
                user = db.session().query(User).filter_by(email=email).first()

                print(user)
            except Exception as e:
                # Log.error(str(e))
                raise e

            if user:
                if not check_password_hash(user.password, password):
                    login_error = 'Invalid password'
                else:
                    session['user_info'] = (user.email, user.username)

                    if next_url != '':
                        return redirect(next_url)
                    else:
                        return redirect(url_for('.index'))
            else:
                login_error = 'User does not exist!'

    return render_template('login.html',
                           next_url=next_url,
                           error=login_error,
                           form=form)


@bp.route('/logout')
@login_required
def logout():
    flash('You were logged out')
    # return redirect(url_for('show_entries'))

    session.clear()

    return redirect(url_for('.index'))


class RegistrationForm(Form):
    email = TextField('email',
                      [validators.Required('Email을 입력하세요.'),
                       validators.Length(min=7, max=100, message='7자리 이상 100자리 이하로 입력하세요.')])

    password = PasswordField('New Password',
                             [validators.Required('비밀번호를 입력하세요.'),
                              validators.Length(min=5, max=100, message='6자리 이상 100자리 이하로 입력하세요.')])

    next_url = HiddenField('Next URL')

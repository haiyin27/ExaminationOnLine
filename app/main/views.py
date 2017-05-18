# -*- coding: utf-8 -*-
from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from ..mail import send_email
from . import main
from .forms import NameForm
from flask_login import login_required, login_user

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))

@main.route('/examination')
@login_required
def examination():
    # 判断用户登录状态，显示考试列表
    return render_template('examination.html')

@main.route('/secret')
def secret():
    return 'Only authenticated users are allowed!'
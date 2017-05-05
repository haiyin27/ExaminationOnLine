# -*- coding: utf-8 -*-

from flask import Flask
from flask import session
from flask import redirect
from flask import url_for
from flask import render_template
from flask import make_response
from flask import flash
from flask_moment import Moment
from flask_script import Manager
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Required
from models import User
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)  # pylint: disable=invalid-name

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/hfbank?charset=utf8'
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
app.config['SECRET_KEY'] = 'HfBaNk'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

db = SQLAlchemy(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route("/", methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first();
        if user is None:
            session["known"] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),  known=session.get('known', False))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    resp = make_response(render_template('500.html'), 404)
    resp.headers['X-Something'] = '500'
    return resp

if __name__ == '__main__':
    manager.run()

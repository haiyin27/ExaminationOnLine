# -*- coding: utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
from flask import make_response
from datetime import datetime
from flask_moment import Moment
from flask_script import Manager

app = Flask(__name__)  # pylint: disable=invalid-name

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/")
def index():
    return render_template('index.html', current_time=datetime.utcnow())

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

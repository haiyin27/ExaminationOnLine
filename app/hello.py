# -*- coding: utf-8 -*-
'''
MODEL.PY
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HfBaNk'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/hfbanktest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(
        db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(
        db.String(32),
        nullable=False,
        unique=True,
        server_default='',
        index=True)
    role_id = db.Column(db.Integer, nullable=False, server_default='0')

    def __repr__(self):
        return '<User %r,Role id %r>' % (self.username, self.role_id)

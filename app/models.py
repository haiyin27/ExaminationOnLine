# -*- coding: utf-8 -*-

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from flask_login import login_required

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/hfbank?charset=utf8'

db = SQLAlchemy(app)
manager = Manager(app)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, nullable=False)
    email = db.Column(db.String(320), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    login_at = db.Column(db.Float, nullable=False)
    create_at = db.Column(db.Float, nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


# class Examination(db.Model):
#     __table__ = 'examinations'
#     id = db.Column(db.Integer, primary_key=True)
#     examname = db.Column(db.String(80), unique=True, nullable=False)
#     examdate = db.Column(db.Float, nullable=False)
#     examduration = db.Column(db.Float, index=True, nullable=False)
#     examtype = db.Column(db.Integer, nullable=False)
#
#     login_at = db.Column(db.Float, nullable=False)
#     create_at = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Examination %r>' % self.examname

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



if __name__ == '__main__':
    manager.run()

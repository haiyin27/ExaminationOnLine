# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))
configs = {
    'dev_db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '123456',
        'database': 'hfbank'
    },
    'test_db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '123456',
        'database': 'hfbank'
    },
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '123456',
        'database': 'hfbank'
    },
    'session': {
        'secret': 'HfBaNk'
    }
}
class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://' + configs.get('dev_db').get('user') +\
                              ':' + configs.get('dev_db').get('password') +\
                              '@' + configs.get('dev_db').get('host') +\
                              ':' + str(configs.get('dev_db').get('port'))+\
                              '/' + configs.get('dev_db').get('database')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://' + configs.get('test_db').get('user') +\
                              ':' + configs.get('test_db').get('password') +\
                              '@' + configs.get('test_db').get('host') +\
                              ':' + str(configs.get('test_db').get('port'))+\
                              '/' + configs.get('test_db').get('database')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://' + configs.get('db').get('user') +\
                              ':' + configs.get('db').get('password') +\
                              '@' + configs.get('db').get('host') +\
                              ':' + str(configs.get('db').get('port'))+\
                              '/' + configs.get('db').get('database')



env_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
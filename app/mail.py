# -*- coding: utf-8 -*-
from flask_mail import Mail
from flask_mail import Message
from flask import Flask
from flask import render_template
from flask import current_app
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'cjj727'
app.config['MAIL_PASSWORD'] = 'Hai318Yin409@04'

mail = Mail(app)
app.config['EXAMINATION_MAIL_SUBJECT_PREFIX'] = '[HFBank EXAMINATION系统注册]'
app.config['EXAMINATION_MAIL_SENDER'] = 'EXAMINATION Admin <cjj727@163.com>'
def send_email(to, subject, template, **kwargs):
    with app.app_context():
        msg = Message(app.config['EXAMINATION_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['EXAMINATION_MAIL_SENDER'], recipients=[to])
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = render_template(template + '.html', **kwargs)
        mail.send(msg)

if __name__ == '__main__':
    send_email(app.config['EXAMINATION_MAIL_SENDER'], 'New User', 'mail/new_user', user='haiyin')
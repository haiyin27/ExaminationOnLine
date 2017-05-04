# -*- coding: utf-8 -*-

from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", text="Hello World!")


@app.route('/login')
def login():
    return "Login Html Page."


if __name__ == '__main__':
    app.run(debug=True)
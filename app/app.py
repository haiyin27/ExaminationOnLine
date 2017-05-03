#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)  # pylint: disable=invalid-name


@app.route("/")
def index():
    """
    Hello World!
    """
    return "Hello World!"


def main():
    """
    start the app
    """
    app.run()


if __name__ == '__main__':
    main()

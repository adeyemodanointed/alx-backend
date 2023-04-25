#!/usr/bin/env python3
"""Flask-babel app"""
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configuration class"""
    LANGUAGES = ["en", "fr"]


@app.route('/')
def index():
    """Index route"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()

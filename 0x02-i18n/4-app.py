#!/usr/bin/env python3
"""Flask-babel app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get Locale method and return match"""
    locale_ = request.args.get('locale')
    if locale_ in app.config['LANGUAGES']:
        return locale_
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Index route"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()

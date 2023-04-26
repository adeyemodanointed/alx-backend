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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(userId):
    """Get's user with ID"""
    return users.get(int(userId))


@app.before_request
def before_request():
    """Get user before request"""
    user = get_user(request.args.login_as)
    g.user = user


@babel.localeselector
def get_locale():
    """Get Locale method and return match"""
    locale_ = request.args.get('locale')
    if locale_ in app.config['LANGUAGES']:
        return locale_
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """Index route"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()

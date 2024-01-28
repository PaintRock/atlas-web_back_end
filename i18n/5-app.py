#!/usr/bin/env python3
"""Babel object in da house"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import g, request

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """Config class"""
    LANGUAGES = "en", "fr"
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
"""not sure why this makes this work"""


@babel.localeselector
def get_locale():
    """get locale function"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(user_id):
    """returns users from dict or none"""
    return users.get(user_id)


@app.before_request
def before_request():
    """get user id from the login as"""
    user_id = request.args.get('login_as', type=int)
    g.user = get_user(user_id)


@app.route('/')
def root():
    """basic Flask"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)

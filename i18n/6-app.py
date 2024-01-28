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
    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['LANGUAGES']:
        return url_locale

    if g.user and 'locale' in g.user and g.user
    ['locale'] in app.config['LANGUAGES']:

        return g.user['locale']

    header_locale = request.accept_languages.best_match(
        app.config['LANGUAGES'])
    if header_locale:
        return header_locale

    return app.config['BABEL_DEFAULT_LOCALE']


def get_user(user_id):
    """returns users from dict or none"""
    if users and 'locale' in users and users
    return users.get(user_id)


@app.before_request
def before_request():
    user_id = request.args.get('login_as', type=int)
    g.user = users.get(user_id)


@app.route('/')
def root():
    """basic Flask"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(debug=True)

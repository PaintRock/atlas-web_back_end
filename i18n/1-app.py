#!/usr/bin/env python3
"""Babel object in da house"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import g, request

app = Flask(__name__)
babel = Babel(app)


class Config():
    """Config class"""
    LANGUAGES = "en", "fr"
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    """get locale function"""
    return.request.accept_languages.best_match(['en', 'fr'])


app.config.from_object(Config)
"""Use that class as config for Flask app"""


@app.route('/')
def root():
    """basic Flask"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()

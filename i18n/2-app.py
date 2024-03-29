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


app.config.from_object(Config)
"""not sure why this makes this work"""


@babel.localeselector
def get_locale():
    """get locale function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def root():
    """basic Flask"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()

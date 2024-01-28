#!/usr/bin/env python3
"""Babel object in da house"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """Config class"""
    LANGUAGES = "en", "fr"
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
"""Use that class as config for Flask app"""


@app.route('/')
def root():
    """basic Flask"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()

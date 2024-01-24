#!/usr/bin/env python3
"""App.py"""
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def welcome():
    """has a single get route = '/'"""
    message = {"message": "Bienvenue"}
    return jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

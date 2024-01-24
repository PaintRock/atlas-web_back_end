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


@app.route("/users", methods=["POST"])
def register_users():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """Implement a login function to respond
    to the POST / sessions route
    Should contain form dat with email and pswrd
    fields
    Use flash.abourt to resond with 401 if
    incorrect"""
    form_data = request.form

    if not email or not password:
        return jsonify(("message: missing credetials")), 400
    else:

        email = request.form.get("email")
        pswd = request.form.get("password")

        if AUTH.valid_login(email, pswd) is False:
            abort(401)
        else:
            session_id = AUTH.create_session(email)
            response = jsonify({
                "email": email,
                "message": "logged in"
            })
            response.set_cookie('session_id', session_id)

            return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

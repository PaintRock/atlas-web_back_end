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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def login() -> str:
    """Implement a login function to respond
    to the POST / sessions route
    Should contain form dat with email and pswrd
    fields
    Use flash.abourt to resond with 403 if
    incorrect"""
    form_data = request.form

    if "email" not in form_data:
        return jsonify({"message": "email required"}), 403
    elif "password" not in form_data:
        return jsonify({"message": "password required"}), 403
    else:

        email = request.form.get("email")
        pswd = request.form.get("password")

        if AUTH.valid_login(email, pswd) is False:
            abort(403)
        else:
            session_id = AUTH.create_session(email)
            response = jsonify({
                "email": email,
                "message": "logged in"
            })
            response.set_cookie('session_id', session_id)

            return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def log_out() -> None:
    """Find the user with the requested session ID.
    If the user exists destroy the session and redirect the user to GET /.
    If the user does not exist, respond with a 403 HTTP status.
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """user profilee endpoint
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None:
        abort(403)
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """generate a token and respond with a 200 HTTP status"""
    try:
        email = request.form['email']
    except KeyError:
        abort(403)

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    msg = {"email": email, "reset_token": reset_token}

    return jsonify(msg), 200


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ Update the password
    PUT /reset_password
    """
    try:
        email = request.form['email']
        reset_token = request.form['reset_token']
        new_password = request.form['new_password']
    except KeyError:
        abort(400)

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)

    msg = {"email": email, "message": "Password updated"}
    return jsonify(msg), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

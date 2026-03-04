from flask import request, render_template, redirect, url_for, make_response
from . import auth

def validate(email, pswd):
    if "@" not in email:
        return False
    if len(pswd) < 5 or len(pswd) > 8:
        return False
    return True

@auth.route("/login")
def login():
    message = request.args.get("message")
    return render_template("login.html", message=message)

@auth.route("/submit", methods=["POST"])
def submit():
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    if not validate(email, password):
        return redirect(url_for("auth.login", message="invalid login credentials"))
    response = make_response(redirect(url_for("auth.success")))
    response.set_cookie("username", username)
    return response

@auth.route("/success")
def success():
    username = request.cookies.get("username", "user")
    visits = int(request.cookies.get("visits", 0)) + 1
    
    response = make_response(
        f"{username}: {visits}"
    )

    response.set_cookie("visits", str(visits))

    return response
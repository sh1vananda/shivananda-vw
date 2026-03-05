from flask import render_template, request, session, redirect, url_for
from . import auth

users = {
    "abc": "abc123",
    "def": "def123"
}

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("products.get_products"))
        
    return render_template("login.html")

@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
        
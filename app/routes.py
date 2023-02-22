from flask import render_template, request, flash, url_for, redirect
from werkzeug.security import check_password_hash
from flask_login import login_user, login_manager, logout_user, login_required, current_user

from .forms import LoginForm, SignupForm
from app import app


@app.route("/")
@app.route("/main")
def index():
    return render_template("main.html")


# @app.route("/login")
# def login():
#
#     return render_template("login.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        nickname = request.form["nickname"]
        password = request.form["password"]
        remember = True if request.form.get("remember") else False

        user = session.query(User).where(User.nickname == nickname).first()
        is_password_correct = False

        if user:
            is_password_correct = check_password_hash(user.password, password)
        if not user or not is_password_correct:
            flash("Try again and check your login details")
            return redirect(url_for("login"))

        login_user(user)
        return redirect("main")
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("main")


@app.route("/signup")
def signup():
    form = SignupForm()
    return render_template("signup.html", form=form)


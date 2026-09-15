from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import User
from app.forms import RegistrationForm
from werkzeug.security import generate_password_hash


main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')

@main.route("/lost")
def lost():
    return render_template("lost.html")


@main.route("/found")
def found():
    return render_template("found.html")


@main.route("/lost-items")
def lost_items():
    return render_template("lost_items.html")


@main.route("/found-items")
def found_items():
    return render_template("found_items.html")


@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():

        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user:
            flash("An account with this email already exists.", "danger")
            return redirect(url_for("main.register"))

        hashed_password = generate_password_hash(form.password.data)

        user = User(
            name=form.name.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for("main.login"))

    return render_template("register.html", form=form)
from flask import Blueprint, render_template

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


from flask import Blueprint, render_template, redirect, url_for, flash
from app import db
from app.models import User, Item
from app.forms import RegistrationForm, LoginForm, ItemForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')

@main.route("/lost")
@login_required
def lost():
    return render_template("lost.html")


@main.route("/found")
@login_required
def found():
    return render_template("found.html")


@main.route("/lost-items")
@login_required
def lost_items():
    items = Item.query.filter_by(type='lost').all()
    return render_template("lost_items.html", items = items)

@main.route('/item/<int:item_id>')
def item_detail(item_id):
    item = Item.query.get_or_404(item_id)
    return render_template('item_detail.html', item=item)


@main.route("/found-items")
@login_required
def found_items():
    items = Item.query.filter_by(type='found').all()
    return render_template("found_items.html", items=items)


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


@main.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email = form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user) #Flask-Login internally manages the current user.And in a template, Flask-Login makes current_user available automatically:
            flash("Login successful", "success")
            return redirect(url_for('main.home'))

        flash("Invalid email or password", "danger")

    return render_template('login.html', form = form)



@main.route("/logout")
def logout():
    logout_user()

    flash("You have been logged out.", "info")

    return redirect(url_for("main.home"))


@main.route('/report', methods=['GET', 'POST'])
def report():
    form = ItemForm()

    if form.validate_on_submit():
        item = Item(
            name = form.name.data,
            category = form.category.data,
            location = form.location.data,
            description = form.description.data,
            type = form.type.data,
            user_id = current_user.id
        )
        db.session.add(item)
        db.session.commit()
        flash("Item reported successfully!", "success")
        return redirect(url_for("main.home"))
    return render_template('report.html', form = form)

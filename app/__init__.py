from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_login import LoginManager

db = SQLAlchemy()   #We're creating our SQLAlchemy database object.db as the connection/interface between Flask and our database.
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id): #user_id is simply the parameter name chosen by us.
    from app.models import User
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lost_found.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login' #If somebody tries to access a protected page without logging in, send them to main.login."

    from app.routes import main
    app.register_blueprint(main)

    with app.app_context():
        from app.models import Item, User
        db.create_all()
    return app

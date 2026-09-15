from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

db = SQLAlchemy()   #We're creating our SQLAlchemy database object.db as the connection/interface between Flask and our database.


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lost_found.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    with app.app_context():
        from app.models import Item, User
        db.create_all()
    return app

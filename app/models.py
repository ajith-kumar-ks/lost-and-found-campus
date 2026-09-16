from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    items = db.relationship("Item", backref="reporter", lazy=True)  #item.reporter could give us the user who reported it. user.items gives all items reported by that user.
    #With lazy=True, SQLAlchemy doesn't fetch the user's items immediately when it fetches the User.It fetches them only when you actually access user.items.
    def __repr__(self):
        return f"<User {self.email}>"

    

class Item(db.Model):   #SQLAlchemy turns that conceptually into a database table:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default="active")
    type = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)   #user_id connects an item to a particular user.


    def __repr__(self):
        return f"<Item {self.name}>"
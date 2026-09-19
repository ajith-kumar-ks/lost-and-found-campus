from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    items = db.relationship("Item", backref="reporter", lazy=True)  #item.reporter could give us the user who reported it. user.items gives all items reported by that user.so backref gives you the reverse direction access.
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
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)   #user_id connects an item to a particular user.db.ForeignKey is database-level connection.

    def __repr__(self):
        return f"<Item {self.name}>"


class Claim(db.Model):
    id = db.column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    claimant_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    status = db.Column(
        db.String(20),
        default="pending"
    )

    item = db.relationship(
        "Item",
        backref="claims"
    )

    claimant = db.relationship(
        "User",
        backref="claims"
    )

    def __repr__(self):
        return f"<Claim {self.id}>"







#     User
#  │
#  ├── user.items ─────→ Items reported by user
#  │
#  └── user.claims ────→ Claims made by user


# Item
#  │
#  ├── item.reporter ──→ User who reported it
#  └── item.claims ────→ Claims made on it


# Claim
#  │
#  ├── claim.item ─────→ Item being claimed
#  └── claim.claimant ─→ User making the claim
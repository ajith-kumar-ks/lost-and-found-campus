from flask import Blueprint, jsonify, request
from app.models import Item
from app import db

api = Blueprint("api", __name__, url_prefix='/api')


@api.route("/items", methods=["GET"])
def get_items():

    items = Item.query.all()

    return jsonify([
        {
            "id": item.id,
            "name": item.name,
            "category": item.category,
            "location": item.location,
            "description": item.description,
            "type": item.type,
            "status": item.status
        }
        for item in items  #List comprehension makes it shorter. Python lets us write the same thing as: [expression for variable in collection]
    ])


@api.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):

    item = Item.query.get_or_404(item_id)

    return jsonify({
        "id": item.id,
        "name": item.name,
        "category": item.category,
        "location": item.location,
        "description": item.description,
        "type": item.type,
        "status": item.status
    })



@api.route("/items", methods=["POST"])
def create_item():

    data = request.get_json() #it converts the incoming JSON into a Python dictionary.

    item = Item(
        name=data["name"],
        category=data["category"],
        location=data["location"],
        description=data["description"],
        type=data["type"],
        user_id=data["user_id"]
    )

    from app import db

    db.session.add(item)
    db.session.commit()

    return jsonify({
        "message": "Item created successfully",
        "item": {
            "id": item.id,
            "name": item.name,
            "category": item.category,
            "location": item.location,
            "description": item.description,
            "type": item.type,
            "status": item.status
        }
    }), 201
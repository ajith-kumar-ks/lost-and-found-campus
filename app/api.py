from flask import Blueprint, jsonify, request
from app.models import Item

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
from flask import Blueprint, jsonify, request
from server.models.restaurant import Restaurant
from server import db

restaurant_controller = Blueprint('restaurant_controller', __name__)

# Get all restaurants
@restaurant_controller.route('/restaurants', methods=['GET'])
def get_all_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "address": r.address
    } for r in restaurants])

# Get a single restaurant by ID
@restaurant_controller.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": [{"id": p.id, "name": p.name, "ingredients": p.ingredients} for p in restaurant.pizzas]
    })

# Delete a restaurant by ID
@restaurant_controller.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204  # No content response

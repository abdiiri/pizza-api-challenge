from flask import Blueprint, jsonify, request, abort
from server.models import Restaurant, RestaurantPizza, Pizza
from server import db

restaurant_bp = Blueprint('restaurant_bp', __name__)

@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "address": r.address
    } for r in restaurants])

@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    pizzas = [{
        "id": rp.pizza.id,
        "name": rp.pizza.name,
        "ingredients": rp.pizza.ingredients
    } for rp in restaurant.restaurant_pizzas]
    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": pizzas
    })

@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    # Delete all related RestaurantPizzas
    RestaurantPizza.query.filter_by(restaurant_id=id).delete()
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
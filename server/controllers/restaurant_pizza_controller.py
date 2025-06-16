from flask import Blueprint, request, jsonify
from server.models import RestaurantPizza, Pizza, Restaurant
from server import db

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Validation
    errors = []
    if price is None or not (1 <= price <= 30):
        errors.append("Price must be between 1 and 30")
    if not pizza_id or not Pizza.query.get(pizza_id):
        errors.append("Pizza not found")
    if not restaurant_id or not Restaurant.query.get(restaurant_id):
        errors.append("Restaurant not found")
    if errors:
        return jsonify({"errors": errors}), 400

    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(rp)
    db.session.commit()

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)
    return jsonify({
        "id": rp.id,
        "price": rp.price,
        "pizza_id": rp.pizza_id,
        "restaurant_id": rp.restaurant_id,
        "pizza": {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        },
        "restaurant": {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
    }), 201
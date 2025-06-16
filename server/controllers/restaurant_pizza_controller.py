from flask import Blueprint, request, jsonify
from server import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    # Validation for price range
    if not (1 <= data['price'] <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    restaurant = Restaurant.query.get(data['restaurant_id'])
    pizza = Pizza.query.get(data['pizza_id'])

    if restaurant and pizza:
        restaurant_pizza = RestaurantPizza(price=data['price'], restaurant_id=data['restaurant_id'], pizza_id=data['pizza_id'])
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify(restaurant_pizza.to_dict()), 201
    return jsonify({"error": "Restaurant or Pizza not found"}), 404

from flask import Blueprint, jsonify
from server.models.pizza import Pizza

pizza_controller = Blueprint('pizza_controller', __name__)

# Get all pizzas
@pizza_controller.route('/pizzas', methods=['GET'])
def get_all_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "ingredients": p.ingredients
    } for p in pizzas])

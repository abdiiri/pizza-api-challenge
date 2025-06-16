from flask import Blueprint

restaurant_bp = Blueprint('restaurant_bp', __name__)

@restaurant_bp.route('/restaurants')
def get_restaurants():
    return "List of restaurants"
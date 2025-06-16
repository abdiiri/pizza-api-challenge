from flask import Flask
from flask_migrate import Migrate
from server import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config')
    db.init_app(app)
    migrate = Migrate(app, db)

    from server.models import restaurant, pizza, restaurant_pizza

    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.pizza_controller import pizza_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    @app.route("/")
    def index():
        return "Hello, Pizza API!"

    return app

app = create_app()
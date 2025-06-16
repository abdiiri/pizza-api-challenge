from flask import Flask
from flask_migrate import Migrate
from server import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config')
    db.init_app(app)
    migrate = Migrate(app, db)

    # Import models so they are registered with SQLAlchemy
    from server.models import restaurant, pizza, restaurant_pizza

    # Import and register blueprints
    from server.controllers.restaurant_controller import restaurant_bp
    app.register_blueprint(restaurant_bp)

    @app.route("/")
    def index():
        return "Hello, Pizza API!"

    return app

app = create_app()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config')  # Make sure config.py exists and is correct

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so they are registered with SQLAlchemy
    from server.models import restaurant, pizza, restaurant_pizza

    # Register blueprints or routes if you have controllers
    # from server.controllers.restaurant_controller import restaurant_bp
    # app.register_blueprint(restaurant_bp)

    return app

# For Flask CLI to discover the app
app = create_app()
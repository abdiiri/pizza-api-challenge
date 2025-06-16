from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from server.controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller

app.register_blueprint(restaurant_controller.bp)
app.register_blueprint(pizza_controller.bp)
app.register_blueprint(restaurant_pizza_controller.bp)

if __name__ == '__main__':
    app.run(debug=True)

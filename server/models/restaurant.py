from server import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    
    # Relationships
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Restaurant {self.name}>"

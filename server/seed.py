from server import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

def seed():
    pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    db.session.add_all([pizza1, pizza2])
    
    restaurant1 = Restaurant(name="Papa John's", address="123 Main St")
    restaurant2 = Restaurant(name="Domino's", address="456 Elm St")
    db.session.add_all([restaurant1, restaurant2])

    db.session.commit()

if __name__ == '__main__':
    seed()

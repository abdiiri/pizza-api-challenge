from server import db
from server.models import Restaurant, Pizza, RestaurantPizza
from server.app import create_app

def seed():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        r1 = Restaurant(name="Pizza Palace", address="123 Main St")
        r2 = Restaurant(name="Slice of Heaven", address="456 Elm St")

        p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
        p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")

        db.session.add_all([r1, r2, p1, p2])
        db.session.commit()

        rp1 = RestaurantPizza(restaurant_id=r1.id, pizza_id=p1.id, price=10.99)
        rp2 = RestaurantPizza(restaurant_id=r1.id, pizza_id=p2.id, price=12.99)
        rp3 = RestaurantPizza(restaurant_id=r2.id, pizza_id=p1.id, price=11.99)

        db.session.add_all([rp1, rp2, rp3])
        db.session.commit()

        print("Database seeded successfully!")

if __name__ == "__main__":
    seed()
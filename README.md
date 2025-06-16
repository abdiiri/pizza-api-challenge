# 🍕 Pizza Restaurant API

This is a RESTful API for a fictional pizza restaurant built with **Flask**, following the **MVC** architecture. It allows you to manage restaurants, pizzas, and the relationship between them.

---

## 🛠️ Technologies Used

- Python 3
- Flask
- SQLAlchemy
- Flask-Migrate
- Pipenv
- SQLite (development)

---

## 📁 Project Structure (MVC Pattern)
├── server/
│ ├── init.py
│ ├── app.py
│ ├── config.py
│ ├── models/
│ │ ├── init.py
│ │ ├── restaurant.py
│ │ ├── pizza.py
│ │ └── restaurant_pizza.py
│ ├── controllers/
│ │ ├── init.py
│ │ ├── restaurant_controller.py
│ │ ├── pizza_controller.py
│ │ └── restaurant_pizza_controller.py
│ └── seed.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
└── README.md

## 2. Set up your virtual environment
 -pipenv install flask flask_sqlalchemy flask_migrate
 -pipenv shell
 
## 3.Set environment variable
-export FLASK_APP=server/app.py
## 4.Initialize and migrate the database
-flask db init
-flask db migrate -m "Initial migration"
-flask db upgrade

## 🚀 Running the App
- flask --app server.app:create_app run --port=5000

- Server will start at http://localhost:5000



## 📥 Example Requests and Responses
✅ GET /restaurants
Request:
Response:

json

[
  {
    "id": 1,
    "name": "Joe's Pizza",
    "address": "123 Main St"
  }
]

## 🧪 Postman Instructions
Open Postman

Click "Import"

Upload: challenge-1-pizzas.postman_collection.json

Use the provided requests to test:

GET /restaurants

GET /restaurants/:id

DELETE /restaurants/:id

GET /pizzas

POST /restaurant_pizzas
# Author
Name : Abdirizak Hassan Farah

GitHub : https://github.com/abdiiri

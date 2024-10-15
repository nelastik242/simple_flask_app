from flask import Flask, request, jsonify
from werkzeug.urls import url_quote
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@db/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Инициализация базы данных и создание таблицы при старте приложения
with app.app_context():
    db.create_all()

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json.get('name')
    if new_user:
        user = User(name=new_user)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created", "id": user.id}), 201
    return jsonify({"error": "Name is required"}), 400

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name} for user in users]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

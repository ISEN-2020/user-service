from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class UserDB(db.Model):
    email = db.Column(db.String, primary_key=True, index=True)
    password_hash = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    is_admin = data.get('is_admin', False)  # Default to False if not provided

    # Check if the user already exists
    if UserDB.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400

    # Hash the password with a salt
    password_hash = generate_password_hash(password)

    # Create a new user
    new_user = UserDB(email=email, password_hash=password_hash, is_admin=is_admin)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# Login endpoint with admin/customer check
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Find the user by email
    user = UserDB.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, password):
        if user.is_admin:
            return True
        else:
            return True
    else:
        return False

# Delete user endpoint
@app.route('/delete', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Find the user by email
    user = UserDB.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, password):
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401

if __name__ == '__main__':
    app.run(debug=True)

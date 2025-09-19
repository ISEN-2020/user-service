import os
from flask_wtf import CSRFProtect
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from pkg_resources import require
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)
# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'change-me')  # pour signer le cookie de session

# User model
class UserDB(db.Model):
    email = db.Column(db.String, primary_key=True, index=True)
    password_hash = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Register endpoint
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email').strip().lower() #change : lowercase et strip pour les espaces
    password = data.get('password')

    # Checks
    ## check email & mdp presents
    if not email or not password:
        return jsonify({"error": "email and password are required"}), 400

    ## user existant
    if UserDB.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400

    # Hash the password with a salt
    password_hash = generate_password_hash(password)

    # Create a new user
    new_user = UserDB(email=email, password_hash=password_hash, is_admin=False) # change : force non admin a la creation du compte
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

'''@app.route('/api/delete', methods=['DELETE'])
def delete_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Find the user by email
    user = UserDB.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, password):
        if user.is_admin:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"error": "user is not an admin"}), 403

    else:
        return jsonify({"error": "Invalid email or password"}), 401
'''
@app.route('/admin/users/delete', methods=['DELETE'])
def admin_delete_user():
    role = session.get('role') # récup si admin ou user
    if not role:
        return jsonify({"error": "unauthenticated"}), 401
    if role != 'admin':
        return jsonify({"error": "forbidden"}), 403

    #target à supprimer
    data = request.get_json(silent=True) or {}
    target_email = (data.get('email') or '').strip().lower()
    if not target_email:
        return jsonify({"error": "target email required"}), 400

    user = UserDB.query.filter_by(email=target_email).first()
    if not user:
        return jsonify({"error": "not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"{target_email} deleted"}), 200

# Login endpoint with admin/customer check
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Find the user by email
    user = UserDB.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, password):
        session['user_id'] = user.id
        session['role'] = user.is_admin
        return jsonify({"success": True, "message": "logged in", "role": session['role']}),200
    else:
        return jsonify({"success": False, "message": "Invalid email or password"}), 401
# Delete user endpoint


@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"successful logout": True})

if __name__ == '__main__':

    app.run(debug=False, host="0.0.0.0")

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
users = {}
next_id = 1


# Home Route
@app.route('/')
def home():
    return "User API is running!"


# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# GET single user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[user_id])


# CREATE user
@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400

    user = {
        "id": next_id,
        "name": data["name"],
        "email": data["email"]
    }

    users[next_id] = user
    next_id += 1

    return jsonify(user), 201


# UPDATE user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])

    return jsonify(users[user_id])


# DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted_user})


if __name__ == '__main__':
    app.run(debug=True)

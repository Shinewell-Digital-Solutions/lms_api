from flask import Flask, request, jsonify
from model.user_model import user_model

app = Flask(__name__)
obj = user_model()

# Insert user
@app.route("/user/insert", methods=['POST'])
def user_addone_controller():
    try:
        return jsonify(obj.user_addone_model(request.form))
    except Exception as e:
        print(f"Insert Error: {e}")
        return jsonify({"error": str(e)}), 500

# Get all users
@app.route("/user/list", methods=['GET'])
def user_getall_controller():
    try:
        result = obj.user_getall_model()
        return jsonify(result)
    except Exception as e:
        print(f"List Error: {e}")
        return jsonify({"error": str(e)}), 500

# Get user by ID
@app.route("/user/list/<int:id>", methods=['GET'])
def user_getbyid_controller(id):
    try:
        result = obj.user_getbyid_model(id)
        return jsonify(result)
    except Exception as e:
        print(f"GetByID Error: {e}")
        return jsonify({"error": str(e)}), 500

# Update user by ID
@app.route("/user/update/<int:id>", methods=['PUT'])
def user_updatebyid_controller(id):
    try:
        return jsonify(obj.user_updatebyid_model(id, request.form))
    except Exception as e:
        print(f"Update Error: {e}")
        return jsonify({"error": str(e)}), 500

# Delete user by ID
@app.route("/user/delete/<int:id>", methods=['DELETE'])
def user_deletebyid_controller(id):
    try:
        return jsonify(obj.user_deletebyid_model(id))
    except Exception as e:
        print(f"Delete Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

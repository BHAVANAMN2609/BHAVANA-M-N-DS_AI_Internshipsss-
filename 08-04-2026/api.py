from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route (test if server is running)
@app.route('/')
def home():
    return "API is running successfully!"

# GET API example
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Bhavana')  # default name changed
    return jsonify({
        "message": f"Hello, {name}!"
    })

# POST API example
@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()

    return jsonify({
        "status": "success",
        "received_data": data
    })

# PUT API example
@app.route('/api/update/<int:id>', methods=['PUT'])
def update_data(id):
    data = request.get_json()

    return jsonify({
        "message": f"Data with ID {id} updated",
        "new_data": data
    })

# DELETE API example
@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_data(id):
    return jsonify({
        "message": f"Data with ID {id} deleted"
    })

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
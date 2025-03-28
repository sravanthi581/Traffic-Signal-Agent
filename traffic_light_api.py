from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store traffic light status for multiple intersections
traffic_lights = {
    "intersection_1": "Red",
    "intersection_2": "Green",
    "intersection_3": "Yellow"
}

# API Endpoint to Get Traffic Light Status
@app.route('/get_status', methods=['GET'])
def get_status():
    return jsonify(traffic_lights)

# API Endpoint to Change Traffic Light Status
@app.route('/change_status', methods=['POST'])
def change_status():
    data = request.json
    intersection = data.get("intersection")
    new_status = data.get("status")

    if intersection in traffic_lights:
        traffic_lights[intersection] = new_status
        return jsonify({"message": f"Traffic light at {intersection} changed to {new_status}"})
    else:
        return jsonify({"error": "Invalid intersection"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

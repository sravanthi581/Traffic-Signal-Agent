from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/traffic_webhook', methods=['POST'])
def handle_webhook():
    data = request.json  # Get the incoming webhook data
    print("Received data:", data)

    # Process data (e.g., update traffic lights)
    if data["signal"] == "RED":
        response = {"action": "Stop traffic"}
    elif data["signal"] == "GREEN":
        response = {"action": "Allow traffic"}
    else:
        response = {"action": "Invalid signal"}

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)

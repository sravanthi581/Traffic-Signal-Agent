from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect_congestion', methods=['POST'])
def detect_congestion():
    data = request.json
    print(f"Congestion Detection Agent received: {data}")
    return jsonify({"status": "Processed", "message": "Congestion levels updated"})

if __name__ == '__main__':
    app.run(port=5004)

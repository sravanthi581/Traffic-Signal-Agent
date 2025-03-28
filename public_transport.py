from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/optimize_transport', methods=['POST'])
def optimize_transport():
    data = request.json
    print(f"Public Transport Optimization received: {data}")
    return jsonify({"status": "Processed", "message": "Bus lane priority adjusted"})

if __name__ == '__main__':
    app.run(port=5002)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/control_traffic', methods=['POST'])
def control_traffic():
    data = request.json
    print(f"Central Traffic Controller received: {data}")
    return jsonify({"status": "Processed", "message": "Traffic signals adjusted"})

if __name__ == '__main__':
    app.run(port=5001)

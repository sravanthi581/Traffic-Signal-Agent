from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/priority_emergency', methods=['POST'])
def priority_emergency():
    data = request.json
    print(f"Emergency Vehicle Priority received: {data}")
    return jsonify({"status": "Processed", "message": "Emergency route cleared"})

if __name__ == '__main__':
    app.run(port=5003)

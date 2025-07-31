from flask import Flask, jsonify, request
from signal_generator import generate_best_signal

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Binary Signal Bot Running"

@app.route('/signal', methods=['POST'])
def signal():
    data = request.json
    asset = data.get('asset')
    interval = data.get('interval')
    if not asset or not interval:
        return jsonify({"error": "asset and interval required"}), 400

    result = generate_best_signal(asset, interval)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

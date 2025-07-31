from flask import Flask, jsonify
from signal_generator import generate_best_signal

app = Flask(__name__)

@app.route('/api/best_signal', methods=['GET'])
def best_signal():
    signal = generate_best_signal()
    return jsonify(signal)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

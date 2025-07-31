# app.py
from flask import Flask, jsonify
from signal_generator import generate_signal

app = Flask(__name__)

@app.route("/api/best_signal")
def best_signal():
    best = generate_signal()  # You can expand to loop over symbols/timeframes
    return jsonify(best)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

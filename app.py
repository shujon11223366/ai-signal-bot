from flask import Flask, render_template, jsonify
from signals.signal_engine import generate_signals

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api/signals')
def api_signals():
    signals = generate_signals()
    return jsonify(signals)

if __name__ == "__main__":
    app.run(debug=True)
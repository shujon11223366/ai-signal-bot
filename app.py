from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Render!"

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render provides PORT dynamically
    app.run(host='0.0.0.0', port=port)
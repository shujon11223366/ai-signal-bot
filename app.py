from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ Bot is running on Render!"

@app.route("/signal", methods=["POST"])
def receive_signal():
    data = request.json
    print("📩 Signal received:", data)
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render provides this env variable
    app.run(host="0.0.0.0", port=port)
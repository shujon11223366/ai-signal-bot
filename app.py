from flask import Flask
import threading
from telegram_bot import run_bot
from signal_generator import generate_signals

app = Flask(__name__)
latest_signals = {}

def refresh_loop():
    while True:
        try:
            latest_signals.update(generate_signals())
            print("Signals refreshed.")
        except Exception as e:
            print(f"Error in refresh loop: {e}")
        time.sleep(30)

threading.Thread(target=refresh_loop, daemon=True).start()
threading.Thread(target=run_bot, daemon=True).start()

@app.route('/')
def home():
    return "Trading bot is active."

if __name__ == "__main__":
    app.run()
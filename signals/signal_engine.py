import json
from utils.indicators import get_rsi_signal, get_macd_signal

def generate_signals():
    # Simulated example — Replace with real API data
    signal_data = {
        "BTC/USDT": {
            "1min": get_rsi_signal("BTC", "USDT", "1min"),
            "5min": get_macd_signal("BTC", "USDT", "5min")
        },
        "ETH/USDT": {
            "1min": get_rsi_signal("ETH", "USDT", "1min"),
            "5min": get_macd_signal("ETH", "USDT", "5min")
        }
    }

    # Optionally write to cache
    with open("signals/signals_cache.json", "w") as f:
        json.dump(signal_data, f, indent=2)

    return signal_data

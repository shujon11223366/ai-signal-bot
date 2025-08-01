def get_rsi_signal(asset, quote, timeframe):
    # Simulate RSI-based signal
    import random
    value = random.randint(20, 80)
    if value < 30:
        return "BUY"
    elif value > 70:
        return "SELL"
    else:
        return "HOLD"

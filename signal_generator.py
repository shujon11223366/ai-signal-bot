import pandas as pd
import pandas_ta as ta
import requests

def fetch_candles(asset, interval, limit=100):
    # Example: Use Binance API for historical data
    url = f"https://api.binance.com/api/v3/klines?symbol={asset}&interval={interval}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    # Parse into DataFrame
    df = pd.DataFrame(data, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])
    df['close'] = pd.to_numeric(df['close'])
    return df

def generate_best_signal(asset, interval):
    df = fetch_candles(asset, interval)
    close = df['close']

    # Simple example: Moving Average Crossover Strategy
    ma_fast = ta.sma(close, length=5)
    ma_slow = ta.sma(close, length=20)

    if ma_fast.iloc[-1] > ma_slow.iloc[-1] and ma_fast.iloc[-2] <= ma_slow.iloc[-2]:
        signal = "BUY"
        confidence = 0.9
    elif ma_fast.iloc[-1] < ma_slow.iloc[-1] and ma_fast.iloc[-2] >= ma_slow.iloc[-2]:
        signal = "SELL"
        confidence = 0.9
    else:
        signal = "NO SIGNAL"
        confidence = 0.0

    return {
        "asset": asset,
        "interval": interval,
        "signal": signal,
        "confidence": confidence
    }

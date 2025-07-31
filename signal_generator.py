# signal_generator.py
import requests
import pandas as pd
import pandas_ta as ta

def fetch_ohlcv(symbol='BTCUSDT', interval='5m', limit=100):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_volume', 'taker_buy_quote_volume', 'ignore'
    ])
    df['close'] = pd.to_numeric(df['close'])
    return df

def generate_signal(symbol='BTCUSDT', interval='5m'):
    df = fetch_ohlcv(symbol, interval)
    df.ta.rsi(length=14, append=True)
    df.ta.macd(append=True)
    df.ta.ema(length=21, append=True)

    latest = df.iloc[-1]
    rsi = latest['RSI_14']
    macd = latest['MACD_12_26_9']
    macdsignal = latest['MACDs_12_26_9']
    price = latest['close']
    ema = latest['EMA_21']

    signal = "NO TRADE"
    confidence = 50

    if rsi < 30 and macd > macdsignal and price > ema:
        signal = "CALL"
        confidence = 85
    elif rsi > 70 and macd < macdsignal and price < ema:
        signal = "PUT"
        confidence = 85

    return {
        "asset": symbol,
        "interval": interval,
        "signal": signal,
        "confidence": confidence
    }
git add signal_generator.py
git commit -m "fix: handle missing indicators and prevent 500 error"
git push

import requests
import pandas as pd
import pandas_ta as ta

ASSETS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "LTCUSDT"]
INTERVALS = ["1m", "3m", "5m", "15m"]

def fetch_ohlcv(symbol, interval='5m', limit=100):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data, columns=[
        'open_time', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_volume', 'taker_buy_quote_volume', 'ignore'
    ])
    df['close'] = pd.to_numeric(df['close'])
    return df

def generate_signal(df):
    df.ta.rsi(length=14, append=True)
    df.ta.macd(append=True)
    df.ta.ema(length=21, append=True)

    latest = df.iloc[-1]
    rsi = latest.get('RSI_14')
    macd = latest.get('MACD_12_26_9')
    macdsignal = latest.get('MACDs_12_26_9')
    price = latest['close']
    ema = latest.get('EMA_21')

    if rsi is None or macd is None or macdsignal is None or ema is None:
        return "NO SIGNAL"

    if rsi < 30 and macd > macdsignal and price > ema:
        return "CALL"
    elif rsi > 70 and macd < macdsignal and price < ema:
        return "PUT"
    else:
        return "NO SIGNAL"

def generate_best_signal():
    for asset in ASSETS:
        for interval in INTERVALS:
            try:
                df = fetch_ohlcv(asset, interval)
                signal = generate_signal(df)
                if signal in ["CALL", "PUT"]:
                    return {
                        "asset": asset,
                        "interval": interval,
                        "signal": signal,
                        "confidence": 85
                    }
            except Exception as e:
                print(f"Error for {asset} {interval}: {e}")
                continue

    return {
        "asset": "N/A",
        "interval": "N/A",
        "signal": "NO SIGNAL",
        "confidence": 0
    }

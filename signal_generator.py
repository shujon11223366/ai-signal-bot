from utils.scraper import get_all_pairs

def generate_signals():
    # Basic signal logic — use ML logic here if needed
    signals = {}
    pairs = get_all_pairs()

    for pair in pairs:
        action = "BUY" if hash(pair) % 2 == 0 else "SELL"
        signals[pair] = action

    return signals
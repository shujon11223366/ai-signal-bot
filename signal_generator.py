def generate_signals():
    # Mock logic — replace with ML model or signal algorithm
    from utils.scraper import get_all_pairs
    signals = {}
    for pair in get_all_pairs():
        signals[pair] = "Buy" if hash(pair) % 2 == 0 else "Sell"
    return signals
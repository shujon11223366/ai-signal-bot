import requests
from bs4 import BeautifulSoup

def get_all_pairs():
    url = "https://pocketoption.com/en/trading/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    pairs = []
    for tag in soup.find_all(class_="asset-name"):
        pair = tag.text.strip()
        if pair:
            pairs.append(pair)
    return pairs
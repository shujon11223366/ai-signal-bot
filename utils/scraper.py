import requests
from bs4 import BeautifulSoup

def get_all_pairs():
    url = "https://pocketoption.com/en/trading/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    pairs = []
    for tag in soup.find_all(class_="asset-name"):
        name = tag.text.strip()
        if name:
            if "OTC" in name or name.lower().endswith("otc"):
                name += " (OTC)"
            pairs.append(name)

    return pairs
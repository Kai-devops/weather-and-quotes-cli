import requests


def get_random_quote():
    url = "https://zenquotes.io/api/random"

    response = requests.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()[0]
    return data["q"], data["a"]

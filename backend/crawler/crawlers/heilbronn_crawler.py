import requests
from bs4 import BeautifulSoup


def crawl_heilbronn(url):

    events = []

    print("Crawling Heilbronn events")

    response = requests.get(url, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    cards = soup.select("div.event__content")

    for card in cards:

        raw_text = card.get_text(separator=" ", strip=True)

        link = card.select_one("a")

        event_url = None
        if link and link.get("href"):
            event_url = "https://www.heilbronn.de" + link.get("href")

        events.append({
            "raw_text": raw_text,
            "source_url": url,
            "event_url": event_url
        })

    return events
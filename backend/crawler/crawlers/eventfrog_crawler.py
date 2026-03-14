import requests
from bs4 import BeautifulSoup


def crawl_eventfrog(url):

    events = []

    print("Crawling Eventfrog")

    response = requests.get(url, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    cards = soup.select("a.event-list__events__tile")

    for card in cards:

        raw_text = card.get_text(separator=" ", strip=True)

        event_url = card.get("href")

        if event_url:
            event_url = "https://eventfrog.de" + event_url

        events.append({
            "raw_text": raw_text,
            "source_url": url,
            "event_url": event_url
        })

    return events
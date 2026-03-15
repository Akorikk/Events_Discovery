import requests
from bs4 import BeautifulSoup


def crawl_stimme(url):

    events = []

    print("Crawling Stimme events")

    try:

        response = requests.get(url, timeout=15)

        soup = BeautifulSoup(response.text, "html.parser")

        cards = soup.select("div.content-card-wrap")

        for card in cards:

            raw_text = card.get_text(separator=" ", strip=True)

            if len(raw_text) < 40:
                continue

            events.append({
                "raw_text": raw_text,
                "source_url": url
            })

    except Exception as e:

        print("Stimme crawler error:", e)

    return events
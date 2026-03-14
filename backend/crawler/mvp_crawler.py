import requests
from bs4 import BeautifulSoup


def crawl_mvp(url):

    events = []

    print(f"Crawling MVP: {url}")

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        cards = soup.select(".abl-entry-wrapper")

        for card in cards:
            text = card.get_text(separator=" ", strip=True)

            if len(text) < 60:
                continue

            events.append({
                "raw_text": text,
                "source_url": url
            })

    except Exception as e:
        print(f"MVP crawler error: {e}")

    return events
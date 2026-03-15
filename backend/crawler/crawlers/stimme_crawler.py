import requests
from bs4 import BeautifulSoup


def crawl_stimme(url):

    events = []

    print("Crawling Stimme events")

    try:

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        cards = soup.select(".content-card-wrap")

        for card in cards:

            title = card.select_one("h3")
            title = title.get_text(strip=True) if title else ""

            meta = card.select_one(".content-card-date-location")
            meta = meta.get_text(" ", strip=True) if meta else ""

            description = card.select_one("p")
            description = description.get_text(strip=True) if description else ""

            raw_text = f"{title} {meta} {description}"

            if len(raw_text) < 30:
                continue

            events.append({
                "raw_text": raw_text,
                "source_url": url
            })

    except Exception as e:

        print("Stimme crawler error:", e)

    return events
import requests
from bs4 import BeautifulSoup


def crawl_mvp(base_url):

    events = []
    page = 1

    while True:

        url = f"{base_url}?page={page}"

        print(f"Crawling MVP page {page}")

        response = requests.get(url, timeout=15)
        soup = BeautifulSoup(response.text, "html.parser")

        cards = soup.select(".abl-entry-wrapper")

        if not cards:
            break

        for card in cards:

            raw_text = card.get_text(separator=" ", strip=True)

            if len(raw_text) < 40:
                continue

            events.append({
                "raw_text": raw_text,
                "source_url": base_url
            })

        page += 1

        if page > 10: 
            break

    return events
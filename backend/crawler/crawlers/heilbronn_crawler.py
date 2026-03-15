"""import requests
from bs4 import BeautifulSoup


def crawl_heilbronn(url):

    events = []

    print("Crawling Heilbronn events")

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        cards = soup.select("div.event")

        for card in cards:

            raw_text = card.get_text(separator=" ", strip=True)

            if len(raw_text) < 40:
                continue

            link = card.select_one("a")

            event_url = None
            if link and link.get("href"):
                event_url = "https://www.heilbronn.de" + link.get("href")

            events.append({
                "raw_text": raw_text,
                "source_url": url,
                "event_url": event_url
            })

    except Exception as e:
        print("Heilbronn crawler error:", e)

    return events """

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def crawl_heilbronn(url):

    events = []

    print("Crawling Heilbronn events (JS website)")

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)

            page = browser.new_page()

            page.goto(url)

            # wait for javascript to load
            page.wait_for_timeout(5000)

            html = page.content()

            soup = BeautifulSoup(html, "html.parser")

            cards = soup.select("article, .event, .veranstaltung")

            for card in cards:

                raw_text = card.get_text(separator=" ", strip=True)

                if len(raw_text) < 40:
                    continue

                events.append({
                    "raw_text": raw_text,
                    "source_url": url
                })

            browser.close()

    except Exception as e:

        print("Heilbronn crawler error:", e)

    return events
"""import requests
from bs4 import BeautifulSoup
from backend.crawler.source import EVENT_SOURCES


def crawl_all_sources():

    all_events = []

    for url in EVENT_SOURCES:

        print(f"\nCrawling source: {url}")

        try:
            response = requests.get(url, timeout=10)

            soup = BeautifulSoup(response.text, "html.parser")

            text = soup.get_text(separator="\n")

            lines = text.split("\n")

            for line in lines:

                line = line.strip()

                # ignore very small text
                if len(line) < 40:
                    continue

                all_events.append({
                    "raw_text": line,
                    "source_url": url
                })

        except Exception as e:

            print("Crawler error:", url, e)

    return all_events"""

import requests
from bs4 import BeautifulSoup
from backend.crawler.source import EVENT_SOURCES


def crawl_all_sources():

    all_events = []

    for url in EVENT_SOURCES:

        print(f"\nCrawling source: {url}")

        try:
            response = requests.get(url, timeout=15)

            soup = BeautifulSoup(response.text, "html.parser")

        
            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()

            blocks = soup.stripped_strings

            seen = set()   

            for block in blocks:

                text = block.strip()

                # skip duplicates
                if text in seen:
                    continue

                seen.add(text)

                # filter by length only
                if 40 <= len(text) <= 300:

                    all_events.append({
                        "raw_text": text,
                        "source_url": url
                    })

        except Exception as e:

            print("Crawler error:", url, e)

    return all_events
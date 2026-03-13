import requests
from bs4 import BeautifulSoup


def crawl_mvp_events():

    url = "https://www.mvp.de/heilbronn/veranstaltungen/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    events = []

    event_blocks = soup.find_all("div", class_="abl-entry-wrapper")

    for event in event_blocks:

        title = event.get_text(strip=True)

        events.append({
            "raw_text": title,
            "source_url": url
        })

    return events
from backend.crawler.source import EVENT_SOURCES
from backend.crawler.crawlers.mvp_crawler import crawl_mvp
from backend.crawler.crawlers.eventfrog_crawler import crawl_eventfrog
from backend.crawler.crawlers.heilbronn_crawler import crawl_heilbronn


def run_crawlers():

    all_events = []

    for url in EVENT_SOURCES:

        print(f"\nRunning crawler for: {url}")

        try:

            if "mvp.de" in url:
                events = crawl_mvp(url)

            elif "eventfrog.de" in url:
                events = crawl_eventfrog(url)

            elif "heilbronn.de" in url:
                events = crawl_heilbronn(url)

            else:
                print("No crawler defined for:", url)
                continue

            print(f"Events found: {len(events)}")

            all_events.extend(events)

        except Exception as e:
            print("Crawler error:", e)

    return all_events
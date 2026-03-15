"""from backend.crawler.source import EVENT_SOURCES
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

from backend.crawler.source import EVENT_SOURCES

from backend.crawler.crawlers.mvp_crawler import crawl_mvp
from backend.crawler.crawlers.eventfrog_crawler import crawl_eventfrog
from backend.crawler.crawlers.stimme_crawler import crawl_stimme


def run_crawlers():

    all_events = []

    for url in EVENT_SOURCES:

        print(f"\nRunning crawler for: {url}")

        try:

            if "mvp.de" in url:
                events = crawl_mvp(url)

            elif "eventfrog.de" in url:
                events = crawl_eventfrog(url)

            elif "stimme.de" in url:
                events = crawl_stimme(url)

            else:
                print("No crawler defined for:", url)
                continue

            print(f"Events found: {len(events)}")

            all_events.extend(events)

        except Exception as e:
            print("Crawler error:", e)

    print("\nTotal events collected:", len(all_events))

    return all_events """

from backend.crawler.source import EVENT_SOURCES

from backend.crawler.crawlers.mvp_crawler import crawl_mvp
from backend.crawler.crawlers.eventfrog_crawler import crawl_eventfrog
from backend.crawler.crawlers.stimme_crawler import crawl_stimme

from concurrent.futures import ThreadPoolExecutor, as_completed


def run_single_crawler(url):

    try:

        if "mvp.de" in url:
            events = crawl_mvp(url)

        elif "eventfrog.de" in url:
            events = crawl_eventfrog(url)

        elif "stimme.de" in url:
            events = crawl_stimme(url)

        else:
            print("No crawler defined for:", url)
            return []

        print(f"{url} → {len(events)} events")

        return events

    except Exception as e:

        print("Crawler error:", url, e)

        return []


def run_crawlers():

    all_events = []

    print("\nStarting parallel crawlers...\n")

    with ThreadPoolExecutor(max_workers=3) as executor:

        futures = [executor.submit(run_single_crawler, url) for url in EVENT_SOURCES]

        for future in as_completed(futures):

            events = future.result()

            all_events.extend(events)

    print("\nTotal events collected:", len(all_events))

    return all_events
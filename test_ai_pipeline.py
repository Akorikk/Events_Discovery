from backend.crawler.heilbronn_crawler import crawl_mvp_events
from backend.extractor.event_extractor import extract_event


events = crawl_mvp_events()

print("RAW EVENTS FOUND:", len(events))

for event in events[:3]:

    structured = extract_event(event["raw_text"])

    structured["source_url"] = event["source_url"]

    print("\nStructured Event:")
    print(structured)
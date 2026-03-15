from backend.crawler.crawler_manager import run_crawlers
from backend.extractor.event_extractor import extract_event
from backend.services.event_service import save_event, raw_event_exists
from backend.database.db import engine
from backend.database.models import Base


# Create database tables if they do not exist
Base.metadata.create_all(bind=engine)

def run_pipeline():

    events = run_crawlers()

    print("RAW EVENTS FOUND:", len(events))

    for event in events:

        raw_text = event["raw_text"]
        source_url = event["source_url"]

        # 🚀 Skip events already processed
        if raw_event_exists(raw_text):
            continue

        structured = extract_event(raw_text)

        if "error" in structured:
            print("AI extraction failed:", structured)
            continue

        # Skip invalid events
        if not structured.get("title"):
            print("Skipping invalid event:", structured)
            continue

        structured["source_url"] = source_url

        print("\nStructured Event:", structured)

        save_event(structured)


if __name__ == "__main__":
    run_pipeline()
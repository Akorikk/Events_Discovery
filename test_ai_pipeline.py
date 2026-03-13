from backend.crawler.heilbronn_crawler import crawl_mvp_events
from backend.extractor.event_extractor import extract_event
from backend.services.event_service import save_event
from backend.database.db import engine
from backend.database.models import Base


# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)


def run_pipeline():

    events = crawl_mvp_events()

    print("RAW EVENTS FOUND:", len(events))

    for event in events[:5]:

        raw_text = event["raw_text"]
        source_url = event["source_url"]

        # Extract structured event using AI
        structured = extract_event(raw_text)

        # Skip if extraction failed
        if "error" in structured:
            print("AI extraction failed:", structured)
            continue

        # Attach source URL
        structured["source_url"] = source_url

        print("\nStructured Event:", structured)

        # Save event to database
        save_event(structured)


if __name__ == "__main__":
    run_pipeline()
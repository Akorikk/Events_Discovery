from backend.database.db import SessionLocal
from backend.database.models import Event
from backend.services.deduplicator import is_duplicate


def raw_event_exists(raw_text):
    """
    Check if this raw event text has already been processed.
    This prevents sending duplicate events to the AI extractor.
    """

    db = SessionLocal()

    existing = db.query(Event).filter(
        Event.description == raw_text
    ).first()

    db.close()

    return existing is not None


def save_event(event_data):
    """
    Save event to database with embedding-based duplicate detection.
    """

    db = SessionLocal()

    # Embedding similarity duplicate detection
    if is_duplicate(event_data):

        print(f"Duplicate detected by embedding: {event_data['title']}")

        db.close()

        return None

    #Save new event
    event = Event(
        title=event_data["title"],
        date=event_data["date"],
        location=event_data["location"],
        description=event_data["description"],
        source_url=event_data["source_url"]
    )

    db.add(event)
    db.commit()

    print(f"Saved event: {event.title}")

    db.close()

    return event
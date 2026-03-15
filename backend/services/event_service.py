from backend.database.db import SessionLocal
from backend.database.models import Event


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

    db = SessionLocal()

    existing = db.query(Event).filter(
        Event.title == event_data["title"],
        Event.date == event_data["date"]
    ).first()

    if existing:
        print(f"Duplicate event skipped: {event_data['title']}")
        db.close()
        return None

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
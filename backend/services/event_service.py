from backend.database.db import SessionLocal
from backend.database.models import Event


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
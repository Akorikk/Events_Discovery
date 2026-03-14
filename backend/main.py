from fastapi import FastAPI
from backend.database.db import engine, SessionLocal
from backend.database.models import Base, Event

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Heilbronn Event Discovery API"}


@app.get("/events")
def get_events():

    db = SessionLocal()

    events = db.query(Event).all()

    result = [
        {
            "title": e.title,
            "date": e.date,
            "location": e.location,
            "description": e.description,
            "source_url": e.source_url
        }
        for e in events
    ]

    db.close()

    return result
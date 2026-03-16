from fastapi import FastAPI, Request
from backend.database.db import engine, SessionLocal
from backend.database.models import Base, Event

app = FastAPI(
    title="Heilbronn Event Discovery API",
    description="API for automatically discovered events in Heilbronn",
    version="1.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)


# Root endpoint
@app.get("/")
def root():
    return {"message": "Heilbronn Event Discovery API is running"}


# Get all events
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


# Webhook receiver (for testing)
@app.post("/webhook")
async def receive_webhook(request: Request):

    data = await request.json()

    print("Webhook received:", data)

    return {
        "status": "success",
        "message": "Webhook received successfully",
        "data": data
    }
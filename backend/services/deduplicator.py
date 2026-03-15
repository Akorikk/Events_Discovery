from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from backend.database.db import SessionLocal
from backend.database.models import Event


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def build_event_text(title, location, date):
    """
    Combine important fields into one text
    for embedding similarity comparison.
    """
    parts = [
        title or "",
        location or "",
        date or ""
    ]

    return " ".join(parts).strip()


def is_duplicate(event_data, threshold=0.85):

    db = SessionLocal()

    existing_events = db.query(Event).all()

    if not existing_events:
        db.close()
        return False

    # Build text for the new event
    new_text = build_event_text(
        event_data["title"],
        event_data["location"],
        event_data["date"]
    )

    # Build texts for existing events
    existing_texts = [
        build_event_text(e.title, e.location, e.date)
        for e in existing_events
    ]

    # Generate embeddings
    embeddings_existing = model.encode(existing_texts)
    embedding_new = model.encode([new_text])

    # Compute similarity
    similarities = cosine_similarity(embedding_new, embeddings_existing)

    max_similarity = similarities.max()

    print("Max similarity:", max_similarity)

    db.close()

    return max_similarity > threshold
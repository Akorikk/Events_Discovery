from fastapi import FastAPI
from backend.database.db import engine
from backend.database.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Heilbronn Event Discovery API"}
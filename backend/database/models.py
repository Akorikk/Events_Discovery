from sqlalchemy import Column, Integer, String, Text
from backend.database.db import Base


class Event(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    date = Column(String)
    time = Column(String)

    location = Column(String)

    description = Column(Text)

    source_url = Column(String)
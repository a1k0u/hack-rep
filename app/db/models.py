from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

from app.db.db import get_engine

Base = declarative_base()

    
class Messages(Base):
    __tablename__ = "Messages"

    id = Column(Integer, primary_key=True)
    message_id: int = Column(Integer)
    user_1: str = Column(String(36))
    user_2: str = Column(String(36))
    photo_path = Column(Text)
    photo_emoji = Column(Integer)


class MatchingUsers(Base):
    __tablename__ = "MatchingUser"

    id = Column(Integer, primary_key=True)
    user = Column(String(36))
    emoji = Column(Integer)


class Session(Base):
    __tablename__ = "Session"

    id = Column(Integer, primary_key=True)
    user_1: int = Column(String(36))
    user_2: int = Column(String(36))


if __name__ == "__main__":
    Base.metadata.create_all(get_engine())

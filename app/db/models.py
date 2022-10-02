from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import declarative_base
from app.db.db import get_engine

Base = declarative_base()


class MessagesUpdates(Base):
    __tablename__ = "MessageUpdates"

    id = Column(Integer, primary_key=True)
    message_id: int = Column(Integer)
    to_user: str = Column(String(36))
    photo = Column(LargeBinary)


class SessionUpdates(Base):
    __tablename__ = "SessionUpdates"

    id = Column(Integer, primary_key=True)
    to_user = Column(String(36))


class ReactionUpdates(Base):
    __tablename__ = "ReactionUpdates"

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer)
    to_user = Column(String(36))
    emoji_id = Column(Integer)


class MatchingUsers(Base):
    __tablename__ = "MatchingUsers"

    id = Column(Integer, primary_key=True)
    user_id = Column(String(36))
    emoji_id = Column(Integer)


class Sessions(Base):
    __tablename__ = "Sessions"

    id = Column(Integer, primary_key=True)
    user_1: int = Column(String(36))
    user_2: int = Column(String(36))
    task: int = Column(Integer)


if __name__ == "__main__":
    Base.metadata.create_all(get_engine())

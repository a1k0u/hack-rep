import uuid
from pydantic import BaseModel
from app.db.models import Base


class Emoji(BaseModel):
    emoji: int


class User(Emoji, BaseModel):
    id: str


class UserTheme(Emoji, BaseModel):
    background: str


class Session(BaseModel):
    user_1: str
    user_2: str


class Message(BaseModel):
    msg_id: int
    to_user: str
    photo: bytes


class Reaction(BaseModel):
    msg_id: int
    to_user: str
    emoji_id: int

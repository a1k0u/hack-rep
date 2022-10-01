import uuid
from pydantic import BaseModel

from app.db.models import Base


class Emoji(BaseModel):
    emoji: int


class User(Emoji, BaseModel):
    id: uuid.UUID


class UserTheme(Emoji, BaseModel):
    backgound: str


class Message(BaseModel):
    msg_id: int
    user_1: uuid.UUID
    user_2: uuid.UUID
    photo: bytes
    photo_rec: int | None



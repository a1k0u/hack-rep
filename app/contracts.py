import uuid
from pydantic import BaseModel


class Emoji(BaseModel):
    emoji: int


class User(Emoji, BaseModel):
    id: uuid.UUID


class UserTheme(Emoji, BaseModel):
    backgound: str

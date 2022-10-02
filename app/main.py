import uuid
import logging
import base64
import os

from fastapi import FastAPI
from fastapi import Body

import app.db.methods as m
import app.utils.json_responses as js
from app.utils.log_tools import get_line_log
from app.utils.emoji import merge_emoji
from app.contracts import Emoji, User, UserTheme, Message, Session, Reaction

app = FastAPI()


@app.get(
    "/find_session", responses={200: js.make_example_response(js.json_find_session)}
)
async def find_session(user_id: str, user_emoji: int):
    """
    find_session
        Checks out information about created session for user.
        If it exists, session will return with id another user.
        Another way tries to create session with others.

    _extra_summary_
        Use it like a long polling.

    Args:
        user_id:
        user_emoji:

    Returns: {
        session: user_id | None
    }
    """

    user = User(id=user_id, emoji=user_emoji)

    session = m.check_session(user)

    logging.debug(get_line_log(user_id, session, "session"))

    if session:
        m.delete_matching(user)
        return {"id": session}
    elif not session and not m.check_matching(user):
        m.create_matching(user)
        return {"id": None}

    new_session = m.create_session(user)
    if new_session:
        m.delete_matching(user)
        return {"id": new_session}

    return {"id": None}


@app.post(
    "/create_emoji", responses={200: js.make_example_response(js.json_created_emoji)}
)
async def create_emoji(emojis: list[int] | None = Body(embed=True)):
    """
    create_emoji
        Gets list of emojis and returns average emoji with background.

    Args:
        emojis (list[Emoji]): users clicked emojis
    """

    emoji = merge_emoji(emojis)

    return {
        "id": emoji,
        "data": "",
    }


@app.post("/create_message")
async def create_message(message: Message):
    """
    create_message
        Gets message and storages that in database.

    _extended_summary_
        Client gets updates every 200 ms to get updates (polling).
    """

    m.create_message(message)


@app.post("/create_reaction")
async def create_reaction(reaction: Reaction):
    """

    Args:
        reaction:

    Returns:

    """

    m.create_reaction(reaction)


@app.delete("/delete_session/{user_id}")
async def delete_session(user_id: str):
    """
    delete_session
        Delete session for user.

    Args:
        user_id: str
    """

    user = User(id=user_id, emoji=0)
    session = m.check_session(user)
    if session:
        m.delete_session(Session(user_1=user_id, user_2=session))

    m.delete_all_user_info(user_id)


@app.delete("/delete")
async def delete():
    m.delete_db(1)

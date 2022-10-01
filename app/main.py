
import uuid
from fastapi import FastAPI
from fastapi import Body
from app.contracts import Emoji, User, UserTheme, Message
import app.db.methods as m


app = FastAPI()


@app.get("/emojis")
async def get_emojis():
    """
    get_emojis 
        Returns list of emojis.

    Returns:
        _type_: {
            emoji: [
                ...
            ]
        }
    """

    # return hard code 
    # emojis from media in binary form

    
    return {
        "emojis": [
            {
                "id": 1,
                "data": "dsadasdada"
            },
            {
                "id": 1,
                "data": "dsadasdada"
            }
        ]
    }


@app.post("/create_emoji")
async def create_emoji(emojis: list[int] | None = Body(embed=True)):
    """
    create_emoji
        Gets list of emojis and returns average emoji with background


    Args:
        emojis (list[Emoji]): users clicked emojis
    """

    background: hex = "#ABCDEF"
    emoji = emojis[0]

    # gets list int emoji
    # returns binary
    
    return {
        "emoji": emoji,
        "background": background
    }


@app.post("/matching")
async def create_matching(user: User):
    """
    match_users 
        Gets user id and formed emotion, after that finds 
        another user able to be matched.

    Args:
        user_id (uuid.UUID): unique user id
        emoji (Emoji): current emoji
    """

    m.create_matching(user)
    res = m.find_session(user)
    if not res:
        return {"session": None}

    m.delete_matching(res["session"], user.id)
    m.create_session(res["session"], user.id)

    return {"session": res}


@app.get("/poll_mathing")
async def find_poll_matching(user: User):
    session = m.find_session(user)
    if session:
        return {"session": session}
    return {"session": None}


@app.post("/create_message")
async def create_message(message: Message):
    """
    create_message
        Gets message and storeges that in database.

    _extended_summary_
        Client gets updates every 200 ms to get updates (polling).
    """
    
    m.create_message(message)


@app.get("/get_update_msg/{user_id}")
async def get_update_msg(user_id):
    """
    get_update
        Get last updates from database for user.
    """
    el = m.take_updated_msg_user(user_id)
    return el


@app.put("/add_msg_emoji/{message_id}")
async def add_msg_emoji(message_id: int):
    ...


@app.post("/create_session")
async def create_session():
    ...


@app.delete("/delete_session")
async def delete_session():
    ...


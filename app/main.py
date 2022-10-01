
import uuid
from fastapi import FastAPI
from app.contracts import Emoji, User, UserTheme


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
    
    return {
        "emojis": [
            1, 2, 3, 4, 5 
        ]
    }


@app.post("/create_emoji")
async def create_emoji(emojis: list[Emoji] | None):
    """
    create_emoji
        Gets list of emojis and returns average emoji with background


    Args:
        emojis (list[Emoji]): users clicked emojis
    """

    background: hex = "#ABCDEF"
    emoji = emojis[0].emoji

    return {
        "emoji": emoji,
        "background": background
    }


@app.post("/matching")
async def match_users(user: User):
    """
    match_users 
        Gets user id and formed emotion, after that finds 
        another user able to be matched.

    Args:
        user_id (uuid.UUID): unique user id
        emoji (Emoji): current emoji
    """

    # Matching

    # create session

    # return json with ids
    
    ...


@app.post("/create_message")
async def create_message():
    """
    create_message
        Gets message and storeges that in database.

    _extended_summary_
        Client gets updates every 200 ms to get updates (polling).
    """
    
    ...


@app.get("/get_update/{user_id}")
async def get_update():
    """
    get_update
        Get last updates from database for user.
    """
    
    ...     


@app.put("/add_msg_emoji/{message_id}")
async def add_msg_emoji(message_id: int):
    ...


@app.post("/create_session")
async def create_session():
    ...


@app.delete("/delete_session")
async def delete_session():
    ...


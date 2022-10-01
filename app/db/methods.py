from typing import Tuple

from app.db.db import connect_to_db
from app.db.models import Messages, MatchingUsers, Session
from app.contracts import Message, User
from sqlalchemy import insert, select, or_, delete


@connect_to_db
def create_message(conn, items: Message):
    stmt = insert(Messages).values(
        message_id=items.msg_id,
        user_1=items.user_1,
        user_2=items.user_2,
        photo_path=items.photo,
        photo_emoji=items.photo_rec
    )

    conn.execute(stmt)


@connect_to_db
def take_updated_msg_user(conn, user_id):
    stmt = select(Messages).where(Messages.user_2 == user_id)
    msgs = conn.execute(stmt).fetchall()
    st = delete(Messages).where(Messages.user_2 == user_id)
    conn.execute(st)
    return conn.execute(stmt).fetchall()


@connect_to_db
def create_matching(conn, user: User):
    st = insert(MatchingUsers).values(
        user=user.id,
        emoji=user.emoji
    )
    conn.execute(st)


@connect_to_db
def find_session(conn, user: User):
    st = select(MatchingUsers)
    users = conn.execute(st).fetchall()
    session = [el["id"] for el in users if el["emoji"] == user.emoji]
    if session:
        return session[0]
    return None


@connect_to_db
def delete_matching(conn, user_1, user_2):
    st1 = delete(MatchingUsers).where(
        MatchingUsers.user == user_1
    )

    st2 = delete(MatchingUsers).where(
        MatchingUsers.user == user_2
    )

    conn.execute(st1)
    conn.execute(st2)


@connect_to_db
def create_session(conn, user_1, user_2):
    st = insert(Session).values(
        user_1=user_1,
        user_2=user_2
    )

    conn.execute(st)


@connect_to_db
def find_session(conn, user: User):
    st = select(Session).where(
        or_(Session.user_1 == user.id,
            Session.user_2 == user.id)
    )

    session = conn.execute(st).fetchone()
    if session:
        return session["user_1"] if session["user_1"] != user.id else session["user_2"]
    return None

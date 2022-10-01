from typing import Tuple
from app.db.db import connect_to_db
from app.db.models import (
    MessagesUpdates,
    MatchingUsers,
    Sessions,
    SessionUpdates,
    ReactionUpdates,
)
from app.contracts import Message, User, Reaction
from sqlalchemy import insert, select, or_, delete, and_, update


def __delete_updated_message(conn, user_id: str):
    stmt = delete(MessagesUpdates).where(MessagesUpdates.to_user == user_id)
    conn.execute(stmt)


def __delete_updated_reaction(conn, user_id):
    stmt = delete(ReactionUpdates).where(ReactionUpdates.to_user == user_id)
    conn.execute(stmt)


def __delete_updated_session(conn, user_id: str):
    stmt = delete(SessionUpdates).where(SessionUpdates.to_user == user_id)
    conn.execute(stmt)


def __add_session_updates(conn, user_id):
    stmt = insert(SessionUpdates).values(to_user=user_id)

    conn.execute(stmt)


def __get_session_info(conn, user_id: str):
    stmt = select(Sessions).where(
        or_(Sessions.user_1 == user_id, Sessions.user_2 == user_id)
    )

    return conn.execute(stmt).fetchone()


@connect_to_db
def create_matching(conn, user: User):
    stmt = insert(MatchingUsers).values(user_id=user.id, emoji=user.emoji)

    conn.execute(stmt)


@connect_to_db
def check_matching(conn, user: User):
    stmt = select(MatchingUsers).where(MatchingUsers.user_id == user.id)
    return conn.execute(stmt).fetchone()


@connect_to_db
def delete_matching(conn, user: User):
    stmt = delete(MatchingUsers).where(MatchingUsers.user_id == user.id)

    conn.execute(stmt)


@connect_to_db
def check_session(conn, user: User):
    stmt = select(Sessions).where(
        or_(Sessions.user_1 == user.id, Sessions.user_2 == user.id)
    )

    sessions = conn.execute(stmt).fetchall()
    if sessions:
        session = sessions[0]
        return ({session["user_1"], session["user_2"]} - {user.id}).pop()

    return None


@connect_to_db
def create_session(conn, user: User):
    stmt = select(MatchingUsers).where(
        and_(MatchingUsers.emoji == user.emoji, MatchingUsers.user_id != user.id)
    )

    suitable_users = conn.execute(stmt).fetchall()
    if not suitable_users:
        return None

    suitable_user = suitable_users[0]["user_id"]

    session = insert(Sessions).values(user_1=suitable_user, user_2=user.id, task=0)

    conn.execute(session)
    return suitable_user


@connect_to_db
def delete_session(conn, session):
    stmt = delete(Sessions).where(
        or_(Sessions.user_1 == session.user_1, Sessions.user_2 == session.user_1)
    )

    conn.execute(stmt)
    __add_session_updates(conn, session.user_2)


@connect_to_db
def create_message(conn, msg: Message):
    stmt = insert(MessagesUpdates).values(
        message_id=msg.msg_id,
        to_user=msg.to_user,
        photo=msg.photo,
    )

    conn.execute(stmt)

    session_info = __get_session_info(conn, msg.to_user)
    task_amount = session_info["task"]

    update_session_info = (
        update(Sessions)
        .values({"task": task_amount + 1})
        .where(or_(Sessions.user_1 == msg.to_user, Sessions.user_2 == msg.to_user))
    )

    conn.execute(update_session_info)


@connect_to_db
def create_reaction(conn, reaction: Reaction):
    stmt = insert(ReactionUpdates).values(
        to_user=reaction.to_user, msg_id=reaction.msg_id, emoji_id=reaction.emoji_id
    )

    conn.execute(stmt)


@connect_to_db
def take_updated_message(conn, user_id: str):
    stmt = select(MessagesUpdates).where(MessagesUpdates.to_user == user_id)
    message = conn.execute(stmt).fetchone()

    if not message:
        return None

    __delete_updated_message(conn, user_id)

    return message


@connect_to_db
def take_updated_session(conn, user_id: str):
    stmt = select(SessionUpdates).where(SessionUpdates.to_user == user_id)
    session = conn.execute(stmt).fetchone()
    __delete_updated_session(conn, user_id)

    return False if session else True


@connect_to_db
def take_updated_reaction(conn, used_id: str):
    stmt = select(ReactionUpdates).where(ReactionUpdates.to_user == used_id)
    reaction = conn.execute(stmt).fetchone()

    if not reaction:
        return None

    __delete_updated_reaction(conn, used_id)

    return reaction


@connect_to_db
def take_updated_task(conn, user_id: str):
    session_info = __get_session_info(conn, user_id)
    if not session_info:
        return None

    task_amount = session_info["task"]

    if (task_amount - 1) % 2 == 1:
        return None

    return "Отпрофь карфку"


@connect_to_db
def delete_all_user_info(conn, user_id: str):
    __delete_updated_session(conn, user_id)
    __delete_updated_message(conn, user_id)
    __delete_updated_reaction(conn, user_id)


@connect_to_db
def delete_db(conn, tnp):
    st1 = delete(MessagesUpdates)
    conn.execute(st1)

    st2 = delete(Sessions)
    conn.execute(st2)

    st3 = delete(MatchingUsers)
    conn.execute(st3)

    st4 = delete(SessionUpdates)
    conn.execute(st4)

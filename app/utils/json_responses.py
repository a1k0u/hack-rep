def make_example_response(json_dict):
    return {
        "description": "Item requested by ID",
        "content": {"application/json": {"example": json_dict}},
    }


json_find_session = {"session": "None | str"}

json_updates = {
    "messages": {
        "id": 1,
        "message_id": 0,
        "to_user": "47e14635-271f-4e4c-ae3a-65e4b08d7ff",
        "photo": "binary_photo",
    },
    "reaction": {
        "id": 1,
        "msg_id": 1,
        "to_user": "47e14635-271f-4e4c-ae3a-65e4b08d7ff",
        "emoji_id": 25,
    },
    "session_open": True,
    "task": "None | str",
}

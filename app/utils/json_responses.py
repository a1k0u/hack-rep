import base64
import requests


def make_example_response(json_dict):
    return {
        "description": "Item requested by ID",
        "content": {"application/json": {"example": json_dict}},
    }


json_emoji = {"items": [{"id": 1, "data": "binary_data"}]}

json_created_emoji = {
    "id": 1,
    "data": "binary_data",
}

json_find_session = {"id": "None | str"}

json_updates = {
    "message": {
        "message_id": 0,
        "photo": "binary_photo",
    },
    "reaction": {
        "message_id": 1,
        "emoji_id": 25,
    },
    "session_open": True,
    "task": "None | str",
}

if __name__ == "__main__":
    with open("/home/a1k0u/Documents/hack-rep/app/static/emoji/11.png", "rb") as file:
        msg = {
            "message_id": 0,
            "to_user": "dafsdfsdfdf",
            "photo": base64.encodebytes(file.read()).decode("utf-8")
        }

    requests.post("http://localhost:8000/create_message", json=msg)

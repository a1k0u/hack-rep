import requests
import base64


def make_example_response(json_dict):
    return {
        "description": "Item requested by ID",
        "content": {"application/json": {"example": json_dict}},
    }


json_emoji = {
    "items": [
        {
            "id": 1,
            "data": "binary_data"
        }
    ]
}

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
    msg = {
        "message_id": 0,
        "to_user": "5BD1BBEC-ABFD-491E-9E34-74B62041237D",
        "photo": ""
    }

    with open("../static/emoji/2.png", "rb") as f:
        msg["photo"] = base64.encodebytes(f.read()).decode("utf-8")
    requests.post("http://localhost:8000/create_message", json=msg)

from functools import lru_cache
from typing import Callable

from sqlalchemy import create_engine
import sqlalchemy.engine


@lru_cache
def get_engine() -> sqlalchemy.engine.Engine:
    engine = create_engine("postgresql+psycopg2://hack_app:1@localhost:5432/hack")

    return engine


def connect_to_db(function: Callable) -> Callable:
    def wrapper(values: dict = None):
        engine = get_engine()
        with engine.begin() as connection:
            result = function(connection, values)
        return result

    return wrapper


if __name__ == "__main__":
    print(get_engine().connect())

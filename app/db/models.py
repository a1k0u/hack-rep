from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

from app.db.db import get_engine

Base = declarative_base()


class Goods(Base):
    __tablename__ = "Goods"

    id = Column(String(36), primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String(32))
    parent_id = Column(String(36))
    price = Column(Integer)
    date = Column(DateTime(timezone=False), nullable=False)


if __name__ == "__main__":
    Base.metadata.create_all(get_engine())

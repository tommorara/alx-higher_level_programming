#!/usr/bin/python3

"""file that defines the City object class."""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """inherits from Base (imported from model_state)"""
    __tablename__ = "cities"
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True,
    )

    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

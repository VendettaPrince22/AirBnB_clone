#!/usr/bin/python3
"""Contains the class `City` inheriting from `BaseModel`"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a city object"""
    state_id = ""
    name = ""

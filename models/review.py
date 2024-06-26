#!/usr/bin/python3
"""COntains the class `Review` inheriting from `BaseModel`"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a review object"""
    place_id = ""
    user_id = ""
    text = ""

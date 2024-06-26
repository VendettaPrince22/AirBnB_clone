#!/usr/bin/python3
"""Contains the class User inheriting from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a user object"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

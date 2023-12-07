#!/usr/bin/python3
"""
Module that defines User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that defines User logic.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

#!/usr/bin/python3
"""
Module that defines Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class that defines Review logic.
    """

    place_id = ""
    user_id = ""
    text = ""

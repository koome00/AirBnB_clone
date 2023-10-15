#!/usr/bin/python3
"""this is the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """public class attributes"""

    place_id: place id
    user_id: user id
    text = ""

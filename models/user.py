#!/usr/bin/python3
"""
Module user.py
Defines class User that
inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class user that inherits from the 
    BaseModel superclass

    attribute:
        email (str): email
        password (str): password
        first_name (str): first name
        last_name (str): last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
#!/usr/bin/python3
"""
This module is used to create a User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class for managing user objects and inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

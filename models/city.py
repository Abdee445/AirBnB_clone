#!/usr/bin/python3
"""
Class that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class used for managing city objects
    """

    state_id = ""
    name = ""

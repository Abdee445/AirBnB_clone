#!/usr/bin/python3
"""
This module is used to create a Review class

"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class used for managing review objects
    
    """

    place_id = ""
    user_id = ""
    text = ""

#!/usr/bin/python3
"""defines class review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """defines a review"""

    place_id = ""
    user_id = ""
    text = ""

#!/usr/bin/python3
"""creates a new user"""

from models.base_model import BaseModel

class User(BaseModel):
    """creates a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """ Initializes User """
        super().__init__()

#!/usr/bin/python3
"""creates a new user"""

from models.base_model import BaseModel

class User(BaseModel):
    """creates a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, id, created_at, updated_at, *args, **kwargs):
        """ Initializes instance of user """
        super().__init__(id, created_at, updated_at, *args, **kwargs)

#!/usr/bin/python3

""" This module contains the BaseModel class """
import uuid
import datetime


class BaseModel:
    """ Base model class """

    def __init__(self, *args, **kwargs):
        """ Initializes class """
        if kwargs is not None:
            for key, value in kwargs.items():
                self.key = value
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = sel.created_at

    def __str__(self):
        """ Returns a string representation """

        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """

        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = datetime.datetime.now().isoformat()
        my_dict["updated_at"] = datetime.datetime.now().isoformat()

        return my_dict

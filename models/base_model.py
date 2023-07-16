#!/usr/bin/python3

""" This module contains the BaseModel class """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Base model class """

    def __init__(self, *args, **kwargs):
        """
        Initializes class

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value,
                                "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            models.storage.new(self)

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

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """

        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = datetime.now().isoformat()
        my_dict["updated_at"] = datetime.now().isoformat()

        return my_dict

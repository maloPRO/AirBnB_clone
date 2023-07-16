#!/usr/bin/python3

""" Filestorage module """
import os
import json

class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns dictionary """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                from models.base_model import BaseModel
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    class_ = BaseModel if class_name == "BaseModel" else None
                    if class_:
                        obj = class_(**value)
                        self.new(obj)
        except FileNotFoundError:
            pass

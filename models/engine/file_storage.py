#!/usr/bin/python3

""" Filestorage module """
import os
import json

class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file """

    __file_path = "models/engine/file.json"
    __objects = {}

    def __init__(self):
        """ initiallises class """

    def all(self):
        """ returns dictionary """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[obj.id] = ""

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as jsonfile:
            json.dump(self.__objects, jsonfile)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if self.__file_path is not None:
            with open(self.__file_path, "r") as jsonfile:
                self.__objects = json.load(jsonfile)


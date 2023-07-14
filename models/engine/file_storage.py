#!/usr/bin/python3

""" Filestorage module """
import os

class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to instances: """

    __file_path = "path/to/*.json"
    __objects = {}

    def __init__(self):
        """ initiallises class """

    def all(self):
        """ returns dictionary """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """


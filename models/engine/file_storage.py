#!/usr/bin/python3
"""Serializes instances to a JSON file and deserializes JSON file to instances"""

import json
from models.base_model import BaseModel

class FileStorage:
    """Saves and retrieves objects from a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class

    def save(self):
        """
        Serializes __objects to the JSON file (self.__file_path)
        """
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dictionary, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (empty if file not exist)
        """
        try:
            with open(self.__file_path, "r") as file:
            dictionary = json.load(file)
            for key, value in dictionary.items():
                self.__objects[key] = BaseModel.from_dict(value)
        except FileNotFoundError:
            pass

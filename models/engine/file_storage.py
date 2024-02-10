#!/usr/bin/python3
"""
Serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel
import models
import os


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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

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
                self.__objects[key] = eval(value["class"])(**value)
        except FileNotFoundError:
            pass

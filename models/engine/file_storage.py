#!/usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """Defines an object with template FileStorage"""
    __file_path = "AirBnB_clone/file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary '__objects' """
        return self.__objects

    def new(self, obj):
        """Sets in '__objects' the obj with standard key"""
        my_obj = obj.__dict__
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"]\
            = my_obj

    def save(self):
        """Serializes '__objects' to JSON file '__file_path' """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f, default=str)

    def reload(self):
        """Deserializes the JSON file to '__objects' """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                self.__objects = json.load(f)

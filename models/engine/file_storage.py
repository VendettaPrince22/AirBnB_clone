#!/usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """Defines an object with template FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary '__objects' """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the obj with standard key"""
        my_obj = obj
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"]\
            = my_obj

    def save(self):
        """Serializes '__objects' to JSON file '__file_path' """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Deserializes the JSON file to '__objects' """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)

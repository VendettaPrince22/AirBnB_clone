#!/usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json
import os
import models.base_model
import models.user


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
            new_dict = {}
            for key in FileStorage.__objects:
                object_dict = FileStorage.__objects[key]
                new_dict.update({key: object_dict.to_dict()})
            json.dump(new_dict, f, indent=2)

    def reload(self):
        """Deserializes the JSON file to '__objects' """
        classes = {
            'BaseModel': models.base_model.BaseModel,
            'User': models.user.User
        }
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                new_dict = json.load(f)
                for key in new_dict:
                    dict_value = classes[new_dict[key]['__class__']](
                        **new_dict[key])
                    FileStorage.__objects[key] = dict_value

#!/usr/bin/python3
"""
Contains the class BaseModel defining all common attributes/
for other classes
"""
import uuid
import datetime


class BaseModel:
    """Defines an object BaseModel
    Args:
        id (string): unique id for each object
        created_at (datetime): time when object is created
        updated_at (datetime): time when object is updated each time
    """
    def __init__(self):
        """Initializes the object BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute 'updated_at' with
          current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__
        of the object"""
        my_dict = {}
        my_dict = dict(**self.__dict__)

        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()

        return my_dict

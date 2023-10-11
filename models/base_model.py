#!/usr/bin/python3
"""
Module base_model.py

Defines class BaseModel
This class deines all common attributes/methods for other classes
"""


import uuid
from datetime import datetime


class BaseModel():
    """
    defines class BaseModel

    Methods:

    Attributes:
        id (str): unique id
        created_at : time created
        updated_at : time updated
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                setattr(self, "id", str(uuid.uuid4()))
            time = datetime.now()
            if "created_at" not in kwargs.keys():
                setattr(self, "created_at", time)
            if "updated_at" not in kwargs.keys():
                setattr(self, "updated_at", time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        returns [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format
                (self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        updates the public
        instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary
        containing all keys/values of __dict__ of the instance:
        """
        dic = dict(**self.__dic__)
        dic['__class__'] = str(self.__class__.__name__)
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return dic

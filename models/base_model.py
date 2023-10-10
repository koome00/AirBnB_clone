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
        pass

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
        dic = {}
        dic['__class__'] = self.__class__.__name__
        
        for key, value in self.__dict__.items():
            if type(value) is datetime:
                dic[key] = value.isoformat()
            else:
                dic[key] = value
        return dic
                


        



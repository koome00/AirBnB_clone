#!/usr/bin/python3
""" file storage"""


import json
from models.base_model import BaseModel



class FileStorage:
    """ this is the file storage that serializesto a
    JSON file and deserialrizes JSON file to instances
    Private class attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}
    all_classes = {"BaseModel": BaseModel}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls:
            return {key: obj for (key, obj) in self.__objects.items()
                    if isinstance(obj, type(cls))}
        return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize __objects to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """ deserialize the file path to JSON file path """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = self.all_classes[value["__class__"]](**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            return

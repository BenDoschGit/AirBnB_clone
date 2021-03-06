#!/usr/bin/python3
"""[This class serializes instances to a JSON file and
deserializes JSON file to instances]
"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import os.path


class FileStorage:
    """[This serializes instances to a JSON file
        and deserializes JSON file to instances]
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """[This Returns the dictonary called __objects]
        """
        return self.__objects

    def new(self, obj):
        """[Adding an object in the dictionary object]

        Args:
            obj: [This is the object set into __objects
            with key <obj class name>.id]
        """
        self.__objects[type(obj).__name__ + "." + str(obj.id)] = obj

    def save(self):
        """[This serializes __objects to the JSON file]
        """
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w") as FILE:
            FILE.write(json.dumps(new_dict))

    def reload(self):
        """[deserializes the JSON file to __objects]
        """
        from models import dict_of_classes
        dict_grayson = {}

        if os.path.isfile(self.__file_path):
            self.__objects = {}
            with open(self.__file_path, "r") as FILE:
                dict_grayson = json.loads(FILE.read())
                for entry in dict_grayson:
                    obj = dict_grayson[entry]
                    obj_cls = dict_of_classes[obj["__class__"]]
                    self.__objects[entry] = obj_cls(**obj)

    @property
    def objects(self):
        """[Getter for __objects to avoid name mangling]
        """
        return self.__objects

    @objects.setter
    def objects(self, new_dict):
        """[Setter for __objects so we can do unittests]
        """
        self.__objects = new_dict

    @property
    def file_path(self):
        """[getter for File path]
        """
        return(self.__file_path)

    @file_path.setter
    def file_path(self, file):
        """[File Path setter idk]
        """
        self.__file_path = file

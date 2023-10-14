#!/usr/bin/env python3
import json
from base_model import BaseModel
from user import User
from place import Place
from amenity import Amenity
from state import State
from city import City
from review import  Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
    }

    def all(self):
        """Returns the dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """Sets the given object in __objects with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    # Here, you would need to implement the logic to create instances
                    # of the corresponding classes based on the class_name and obj_dict.
                    # Once you have the instance, you can set it in __objects using the
                    # obj_id as the key.
        except FileNotFoundError:
            pass


    def serialize(self):
        """
        Serializes the objects stored in the __objects attribute to a JSON file.
        """
        serialized_objects = {}
        for obj_id, obj in self.__objects.items():
            serialized_objects[obj_id] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def deserialize(self):
        """
        Deserializes the JSON file to recreate the objects and store them in the __objects attribute.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                serialized_objects = json.load(file)
                for obj_id, obj_dict in serialized_objects.items():
                    class_name = obj_dict['__class__']
                    cls = models.classes[class_name]
                    obj = cls(**obj_dict)
                    self.__objects[obj_id] = obj


    def count(self, cls=None):
        """
        Returns the number of objects in storage or the number of objects filtered by class.
        """
        if cls is None:
            return len(self.__objects)
        else:
            count = 0
            for obj in self.__objects.values():
                if isinstance(obj, cls):
                    count += 1
            return count

    def all(self, cls=None):
        """
        Returns a dictionary of all objects or a dictionary of objects filtered by class.
        """
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {}
            for obj_id, obj in self.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[obj_id] = obj
            return filtered_objects
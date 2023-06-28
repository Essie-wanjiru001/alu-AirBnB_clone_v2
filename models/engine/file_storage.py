#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
<<<<<<< HEAD
import json
=======
from datetime import datetime
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
>>>>>>> 070b2400c65851cfed794515179027bbfa97752b


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
<<<<<<< HEAD
        if cls is not None:
            cls_objects = {}
            for k, v in FileStorage.__objects.items():
                if k.startswith(cls.__name__):
                    cls_objects.update({k: v})
            return cls_objects
        else:
            return FileStorage.__objects
=======
        if cls is None:
            return FileStorage.__objects
        else:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    obj_dict[key] = value
            return obj_dict
>>>>>>> 070b2400c65851cfed794515179027bbfa97752b

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
<<<<<<< HEAD
            json.dump(temp, f, sort_keys=True, indent=4)

    def delete(self, obj=None):
        """Deletes the object obj if obj is in __objects"""
        if obj is not None:
            for k, v in FileStorage.__objects.items():
                if v is obj:
                    tmp = k
            FileStorage.__objects.pop(tmp)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

=======
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
>>>>>>> 070b2400c65851cfed794515179027bbfa97752b
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
<<<<<<< HEAD
        """Handles storage close"""
        self.reload()
=======
        """display our HBNB data"""
        self.reload()

    def delete(self, obj=None):
        """delete an object"""
        if obj is not None:
            key = obj.__class__.__name__+'.'+obj.id
            if key in self.__objects:
                del self.__objects[key]
>>>>>>> 070b2400c65851cfed794515179027bbfa97752b

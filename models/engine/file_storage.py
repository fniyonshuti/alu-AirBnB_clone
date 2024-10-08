#!/usr/bin/python3
"""
    Define 'FileStorage' class
"""
from models.base_model import BaseModel
from models.city import City
import os.path
import json


class FileStorage:
    """
        Represent an abstracted storage engine.
        Purpose: Provide a way to store objects in a JSON file.
        Attributes:
            __file_path (str): string to represent the path to the JSON file
            __objects (dict): dictionary to store instantiated objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Return '__objects' dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            Add 'obj' to __objects dictionary with key <obj class name>.id
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
            Serialize '__objects' to the JSON file '__file_path'
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """
            Deserialize JSON file '__file_path' to '__objects' dictionary,
            if file exists else the method does nothing.
        """
        try:
            with open(FileStorage.__file_path) as f:
                file_content = f.read().strip()
                if file_content:  # Check if the file is not empty
                    objdict = json.loads(file_content)
                    for o in objdict.values():
                        cls_name = o["__class__"]
                        del o["__class__"]
                        self.new(eval(cls_name)(**o))
                else:
                    print(f"Warning: {FileStorage.__file_path} is empty")
        except FileNotFoundError:
            print(f"Warning: {FileStorage.__file_path} not found")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in {FileStorage.__file_path}: {e}")
        except Exception as e:
            print(f"Unexpected error while reloading data: {e}")

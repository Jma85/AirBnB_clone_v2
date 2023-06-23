#!/usr/bin/python3
<<<<<<< HEAD
"""This module instantiates an object of class FileStorage"""

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
=======
"""Instantiates a storage object.

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
>>>>>>> 0e44d446eca646eddd5ed11387a6fbdb5fb2af75
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
<<<<<<< HEAD
    storage = DBStorage()
else:
=======
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
>>>>>>> 0e44d446eca646eddd5ed11387a6fbdb5fb2af75
    storage = FileStorage()
storage.reload()

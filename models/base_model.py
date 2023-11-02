#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime

class BaseModel:
    """Base class defining common attributes and methods for other classes."""


    def __init__(self):
        """Initialization of the Base instance."""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        
    def __str__ (self):
        """String representation of the object.
        Format: [<class name>] (<self.id>) <self.dict__>"""

        return "[{}] ({}) {}" .format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        """Updates the updated_at attribute with current datetime."""
        self.updated_at = datetime.now()


    def to_dict(self):
        """Convert the object to a dictionary representation of an instance."""
        my_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

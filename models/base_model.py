#!/usr/bin/python3
"""It defines all common attributes/methods for other classes"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """The base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute to the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel object"""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "class": self.__class__.__name__
        }

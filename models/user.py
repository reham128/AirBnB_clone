#!/usr/bin/python3
""" class User that inherits from Superclass BaseModel
this subclass contains user attributes:
email, password, first_name, last_name"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class Representation"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

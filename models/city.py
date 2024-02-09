#!/usr/bin/python3
"""class city which inherits form superclass BaseModel"""


from models.base_model import BaseModel


class City(BaseModel):
    """Class Representation"""
    state_id = ""
    name = ""

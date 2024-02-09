#!/usr/bin/python3
"""Class Review which inherites form superclass BaseModel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Class Representation"""
    place_id = ""
    user_id = ""
    text = ""

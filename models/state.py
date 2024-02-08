#!/usr/bin/python3
"""class State which inherits from the Superclass BaseModel
One attribute represent State name : name"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class representation"""
    name = ""

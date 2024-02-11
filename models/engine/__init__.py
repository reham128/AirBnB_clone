#!/usr/bin/python3
"""Creates a unique FIleStorage for the application"""
from models.engine.file_storage import FileStorage
from models import *

storage = FileStorage()
storage.reload()

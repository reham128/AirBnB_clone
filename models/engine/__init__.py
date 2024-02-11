#!/usr/bin/python3
"""Creates a unique FIleStorage for the application"""
from models.engine.file_storage import FileStorage
import model *

storage = FileStorage()
storage.reload()

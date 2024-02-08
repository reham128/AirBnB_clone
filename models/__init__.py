#!/usr/bin/python3
"""Creates a unique FIleStorage for the package."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

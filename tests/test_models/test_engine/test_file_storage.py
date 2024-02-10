#!/usr/bin/python3
"""
Unittests Module to test the class of FleStorage
"""
import json
import unittest
from models.base_model import BaseModel
import os
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """class unittest to test FileStorage methods"""

    def setUp(self):
        """Initialize FileStorage instance"""
        self.storage = FileStorage()
        self.new_obj = BaseModel()

        """empty storage befor each test"""
        self.storage.__objects = {}

    def tearDown(self):
        """ remove file.json every time after test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_new(self):
        self.storage.new(self.new_obj)
        tmp = "{}.{}".format(self.new_obj.__class__.__name__, self.new_obj.id)
        self.assertIn(tmp, self.storage.all())
        self.assertEqual(self.storage._FileStorage__objects[tmp], self.new_obj)

    def test_save_and_reload(self):
        self.storage.new(self.new_obj)
        self.storage.save()
        self.storage.reload()
        tmp = "{}.{}".format(self.new_obj.__class__.__name__, self.new_obj.id)
        self.assertIn(tmp, self.storage._FileStorage__objects)

    def test_all(self):
        key = self.storage.all()
        self.assertIsNotNone(key)
        self.assertEqual(type(key), dict)

    def test_emptystorage_all(self):
        key = self.storage.all()
        self.assertIsInstance(key, dict)

    def test_reload_none(self):
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()

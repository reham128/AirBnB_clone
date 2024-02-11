#!/usr/bin/python3
"""
Unittest Module to test the class of BaseModel
"""
import unittest
from models import storage
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Defines the test cases for the BaseModel class
    """
    def test_BaseModel_instantiation(self):
        """
        Test case to test if the BaseModel class can be instantiated
        """
        B_M = BaseModel()
        self.assertEqual(B_M, type(BaseModel()))
        self.assertTure(hasattr(B_M, "created_at"))
        self.assertTure(hasattr(B_M, "updated_at"))

    def test_BaseModel_instantiation_with_arg(self):
        """
        Tests if the BaseModel class can be instantiated with arguments
        """
        B_M = BaseModel()
        self.assertIsInstance(B_M.created_at, datetime)
        self.assertIsInstance(B_M.updated_at, datetime)

    def test_BaseModel_str(self):
        """
        Test case to test the __str__ method of the BaseModel class
        """
        B_M = BaseModel()
        B_M_str = str(B_M)
        self.assertIn("BaseModel", B_M_str)
        self.assertIn(B_M.id, B_M_str)

    def test_BaseModel_save(self):
        """
        Test case to test the save method of the BaseModel class
        """
        B_M = BaseModel()
        B_M.save()
        self.assertNotEqual(B_M.created_at, B_M.updated_at)

    def test_BaseModel_to_dict(self):
        """
        Test case to test the to_dict method of the BaseModel class
        """
        B_M = BaseModel()
        self.assertEqual(type(B_M.to_dict()["id"]), str)
        self.assertEqual(type(B_M.to_dict()["created_at"]), str)
        self.assertEqual(type(B_M.to_dict()["updated_at"]), str)
        self.assertEqual(type(B_M.to_dict()["__class__"]), str)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Unittests Module to test the class of User
"""
import unittest
from models.base_model import BaseModel
import os
from models.user import User
import sys


class TestUser(unittest.TestCase):
    """testing user class"""
    def setUp(self):
        self.user = User()

    def test_base_inhert(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_attribute(self):
        """to test class attribute"""
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "id"))
        self.assertIsInstance(self.user, User)

    def test_dict(self):
        new_user = self.user.to_dict()
        self.assertIn("created_at", new_user)
        self.assertIn("updated_at", new_user)
        self.assertIsInstance(new_user, dict)

    def test_first_name_type(self):
        self.assertIsInstance(getattr(self.user, "first_name"), str)

    def test_last_name_type(self):
        self.assertIsInstance(getattr(self.user, "last_name"), str)

    def test_password_type(self):
        self.assertIsInstance(getattr(self.user, "password"), str)

    def test_email(self):
        self.assertIsInstance(getattr(self.user, "email"), str)

    def test_have_value(self):
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.email, "")


if __name__ == "__main__":
    unittest.main()

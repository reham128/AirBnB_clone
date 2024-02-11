#!/usr/bin/python3
"""
Unittests Module to test the class of State
"""
import unittest
from models.base_model import BaseModel
import os
from models.state import State
import sys
import datetime


class TestState(unittest.TestCase):
    """ testing state class"""
    def setUp(self):
        self.state = State()

    def test_base_inhert(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_attribute_name(self):
        """to test class  name attribute"""
        self.assertTrue(hasattr(self.state, "name"))

    def test_id(self):
        self.assertTrue(hasattr(self.state, "id"))

    def test_created_at(self):
        self.assertTrue(hasattr(self.state, "created_at"))

    def test_updated_at(self):
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_instance_state(self):
        self.assertIsInstance(self.state, State)

    def test_name_type(self):
        self.assertIsInstance(getattr(self.state, "name"), str)

    def test_str_rep(self):
        """to test string representaion for __str__ method"""
        self.assertIn(self.state.id, str(self.state))
        self.assertIn(self.state.__class__.__name__, str(self.state))
        self.assertIn(str(self.state.__dict__), str(self.state))

    def test_name_assignment(self):
        self.state.name = "Ciro"
        self.assertEqual(self.state.name, "Ciro")

    def test_instanition(self):
        self.assertIs(State, type(State()))


if __name__ == "__main__":
    unittest.main()

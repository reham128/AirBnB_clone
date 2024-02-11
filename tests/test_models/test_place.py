#!/usr/bin/python3
"""
Unittests Module to test the class of Place
"""
import unittest
from models.base_model import BaseModel
import os
from models.place import Place
import sys


class TestPlace(unittest.TestCase):
    """Testin Place class"""
    def setUp(self):
        self.place = Place()

    def test_base_inhert(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_attribute_name(self):
        self.assertTrue(hasattr(self.place, "name"))

    def test_id(self):
        self.assertTrue(hasattr(self.place, "id"))

    def test_created_at(self):
        self.assertTrue(hasattr(self.place, "created_at"))

    def test_updated_at(self):
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_instance_place(self):
        self.assertIsInstance(self.place, Place)

    def test_city_id(self):
        self.assertTrue(hasattr(self.place, "city_id"))

    def test_user_id(self):
        self.assertTrue(hasattr(self.place, "user_id"))

    def test_description(self):
        self.assertTrue(hasattr(self.place, "description"))

    def test_number_rooms(self):
        self.assertTrue(hasattr(self.place, "number_rooms"))

    def test_number_bathrooms(self):
        self.assertTrue(hasattr(self.place, "number_bathrooms"))

    def test_max_guest(self):
        self.assertTrue(hasattr(self.place, "max_guest"))

    def test_price_by_night(self):
        self.assertTrue(hasattr(self.place, "price_by_night"))

    def test_latitude(self):
        self.assertTrue(hasattr(self.place, "latitude"))

    def test_longitude(self):
        self.assertTrue(hasattr(self.place, "longitude"))

    def test_amenity_ids(self):
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_place_instance(self):
        self.assertIsInstance(self.place, Place)


if __name__ == "__main__":
    unittest.main()

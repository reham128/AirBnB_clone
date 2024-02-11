#!/usr/bin/python3
"""
unittests for the City class
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test class for City
    """
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.city = City()

    def test_city_is_instance_of_BaseModel(self):
        """
        Test to see if City is an instance of BaseModel
        """
        self.assertTrue(issubclass(self.city, BaseModel))

    def test_city_has_name_attribute(self):
        """
        Test to see if City has a name attribute
        """
        self.assertTrue(hasattr(self.city, "name"))

    def test_city_has_state_attribute(self):
        """
        Test to see if City has a state_id attribute
        """
        self.assertTrue(hasattr(self.city, "state_id"))


if __name__ == "__main__":
    unittest.main()

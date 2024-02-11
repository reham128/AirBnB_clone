#!/usr/bin/python3
"""unittests for the Amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test class for Amenity"""
    def setUp(self):
        """Set up method that will run before every Test"""
        self.amenity = Amenity()

    def test_amenity_is_subclass_of_BaseModel(self):
        """Test to see if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.amenity, BaseModel))

    def test_amenity_has_name_attribute(self):
        """Test to see if Amenity has a name attribute"""
        self.assertTrue(hasattr(self.amenity, "name"))


if __name__ == "__main__":
    unittest.main()

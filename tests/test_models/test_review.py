#!/usr/bin/python3
"""unittests for the Review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test class for Review"""
    def setUp(self):
        """Set up method that will run before every Test"""
        self.review = Review()

    def test_review_is_subclass_of_BaseModel(self):
        """Test to see if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.review, BaseModel))

    def test_review_has_place_id_attribute(self):
        """Test to see if Review has a place_id attribute"""
        self.assertTrue(hasattr(self.review, "place_id"))

    def test_review_has_user_id_attribute(self):
        """Test to see if Review has a user_id attribute"""
        self.assertTrue(hasattr(self.review, "user_id"))

    def test_review_has_text_attribute(self):
        """Test to see if Review has a text attribute"""
        self.assertTrue(hasattr(self.review, "text"))


if __name__ == "__main__":
    unittest.main()

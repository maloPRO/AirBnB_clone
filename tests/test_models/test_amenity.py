#!/usr/bin/python3

""" Module contains tests for state """
import unittest
import models
from models.amenity import Amenity
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def test_class_name(self):
        new_amenity = Amenity()
        class_name = new_amenity.__class__.__name__

        self.assertEqual(class_name, "Amenity")

#!/usr/bin/python3

""" Module contains tests for state """
import unittest
import models
from models.city import City
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def test_class_name(self):
        new_city = City()
        class_name = new_city.__class__.__name__

        self.assertEqual(class_name, "City")

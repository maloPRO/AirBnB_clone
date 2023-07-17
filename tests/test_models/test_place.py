#!/usr/bin/python3

""" Module contains tests for state """
import unittest
import models
from models.place import Place
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def test_class_name(self):
        new_place = Place()
        class_name = new_place.__class__.__name__

        self.assertEqual(class_name, "Place")

#!/usr/bin/python3

""" Module contains tests for state """
import unittest
import models
from models.review import Review
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def test_class_name(self):
        new_review = Review()
        class_name = new_review.__class__.__name__

        self.assertEqual(class_name, "Review")

#!/usr/bin/python3

""" Base model tests """

import unittest
import models
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_model_name(self):

        my_model = BaseModel()
        my_model.name = "Model one"
        self.assertEqual(my_model.name, "Model one")


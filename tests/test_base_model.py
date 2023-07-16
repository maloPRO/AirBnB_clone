#!/usr/bin/python3

""" Base model tests """

import os
import unittest
import models
from time import sleep
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_model_name(self):

        my_model = BaseModel()
        my_model.name = "Model one"
        self.assertEqual(my_model.name, "Model one")
   
    def test_differrent_created_at(self):
        bm1 = BaseModel()
        sleep(0.1)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)


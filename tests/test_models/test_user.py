#!/usr/bin/python3
""" Module contains tests for state """
import unittest
import models
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def test_class_name(self):
        new_user = User()
        class_name = new_user.__class__.__name__

        self.assertEqual(class_name, "User")

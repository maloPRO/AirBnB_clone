#!/usr/bin/python3

""" Module contains tests for state """
import unittest
import models
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def test_class_name(self):
        new_state = State()
        class_name = new_state.__class__.__name__

        self.assertEqual(class_name, "State")

#!/usr/bin/python3
"""Module containing unittests for State.py"""


import unittest
import datetime
from models.state import State
from models import storage
import os


strptime = datetime.datetime.strptime


class TestState(unittest.TestCase):
    """class to test the State class and its methods"""

    def setUp(self):
        """Happens before each function"""
        self.test_dict = {"created_at": "2021-02-15T16:05:33.443043",
                          "id": "125b2cf3-66d9-4185-b442-e8a49cb7801d",
                          "updated_at": "2021-02-15T16:05:33.443043",
                          "__class__": "State", "name": "", "state_id": ""}
        self.obj = State(**self.test_dict)

    def test_init(self):
        """This is the Unittest for the init of State"""
        self.assertIsInstance(self.obj, State)
        self.assertEqual(self.obj.id, self.test_dict["id"])
        self.assertEqual(self.obj.created_at,
                         strptime(self.test_dict["created_at"],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(self.obj.updated_at,
                         strptime(self.test_dict["updated_at"],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertEqual(self.obj.name, "")
        self.assertIsInstance(self.obj.created_at, datetime.datetime)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.name, str)

        'This is test for else statment'
        self.obj = State()

        self.assertIsInstance(self.obj, State)
        self.assertNotEqual(self.obj.id, "")
        self.assertEqual(self.obj.created_at, self.obj.updated_at)
        self.assertEqual(self.obj.name, "")
        self.assertIsInstance(self.obj.created_at, datetime.datetime)
        self.assertIsInstance(self.obj.updated_at, datetime.datetime)
        self.assertIs(self.obj, storage.objects[type(self.obj).__name__ + "." +
                      str(self.obj.id)])
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.name, str)

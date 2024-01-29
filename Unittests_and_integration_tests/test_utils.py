#!/usr/bin/env python3
""" this is some doc"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """This is the class for the first"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), ("b": 2)),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

#!/usr/bin/env python3
""" this is some doc"""
from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """This is the class for the first"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), ("b": 2)),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ Test method return output """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)


if __name__ == "__main__":
    unittest.main() 

#!/usr/bin/env python3
""" Unittest module Task """
from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """ Class for testing Nested Map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_result):
        """ Test method outputs """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_result)


    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b") 'b')
    ])
    def test_access_nested_map_exception(self, map, path, unexpected_result):
        """Test method raises KeyError"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(unexpected_result, e.exception)


if __name__ == "__main__":
    unittest.main()

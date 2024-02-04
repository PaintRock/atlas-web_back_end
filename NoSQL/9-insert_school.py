#!/usr/bin/env python3
"""function that inserts a new document in a collection"""
from unittest import result


def insert_school(mongo_collection, **kwargs):
    """the pymongo collection object"""
    id = mongo_collection.insert(kwargs)
    return id

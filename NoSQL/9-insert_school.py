#!/usr/bin/env python3
"""function that inserts a new document in a collection"""


def list_all(mongo_collection, **kwargs):
    """the pymongo collection object"""
    id = mongo_collection.insert(kwargs)
    return id

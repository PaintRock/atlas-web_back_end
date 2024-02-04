#!/usr/bin/env python3
"""function that inserts a new document in a collection"""

def list_all(mongo_collection, **kwargs):
    """the pymongo collection object"""
    documents = mongo_collection.insert_one(kwargs)
    id = results.inserted_id
    return id

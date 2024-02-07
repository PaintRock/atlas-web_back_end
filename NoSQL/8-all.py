#!/usr/bin/env python3
"""function that inserts a new document in a collection"""


def list_all(mongo_collection):
    """the pymongo collection object"""
    documents = mongo_collection.find()
    document_list = list(documents)
    return document_list

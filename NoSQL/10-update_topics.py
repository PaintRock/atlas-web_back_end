#!/usr/bin/env python3
"""function that changes all topics of a school document """
from unittest import result

def update_topics(mongo_collection, name, topics):
    """Update topics of a document"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    subject = mongo_collection.find()  
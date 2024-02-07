#!/usr/bin/env python3
"""function that returns a list of schools"""


def schools_by_topic(mongo_collection, topic):
    """Document find list """
    return mongo.collection.find({"topics": topic})

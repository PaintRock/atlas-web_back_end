#!/usr/bin/env python3
"""function that provides stats about Nginx"""


def schools_by_topic(logs, topic):
    """Document find list """
    return mongo_collection.find({"topics": topic})

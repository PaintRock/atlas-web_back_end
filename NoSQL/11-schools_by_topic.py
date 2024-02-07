#!/usr/bin/env python3
""" Script to provide stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient

def count_documents_with_method(collection, method):
    """ Count the number of documents with a specific method """
    return collection.count_documents({"method": method})

def count_documents_with_status_path(collection, method, path):
    """ Count the number of documents with a specific method and path """
    return collection.count_documents({"method": method, "path": path})

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = count_documents_with_method(collection, method)
        print(f"\t{count} {method}")

    status_path_count = count_documents_with_status_path(collection, "GET", "/status")
    print(f"{status_path_count} logs where method=GET path=/status")
    
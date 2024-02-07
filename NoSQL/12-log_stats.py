#!/usr/bin/env python3
""" Write a Python script that provides some stats about
    Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """ Connect to MongoDB"""
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    # Get total count of logs
    total_logs = collection.count_documents({})

    # Count documents for each HTTP method
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    method_counts = {
        method: collection.count_documents({
            'method': method}) for method in methods}

    # Count documents with method=GET and path=/status
    status_check_count = collection.count_documents({
        'method': 'GET', 'path': '/status'})

    # Display stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"method {method}: {count}")
    print(f"{status_check_count} status check")

    # Close MongoDB connection
    client.close()


if __name__ == "__main__":
    log_stats()

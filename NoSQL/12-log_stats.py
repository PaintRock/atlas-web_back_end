#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient
from dump import logs

if __name__ == "__main__":
    log_stats()

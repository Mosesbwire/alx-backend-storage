#!/usr/bin/env python3

# 9-insert_school.py

"""Insert data into a collection"""


def insert_school(mongo_collection, **kwargs):
    """inserts school data into a mongo collection and returns id of inserted document"""
    return mongo_collection.insert_one(kwargs).inserted_id

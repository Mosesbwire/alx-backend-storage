#!/usr/bin/env python3

# 8-all.py

"""retrieves data from a mongo collection"""


def list_all(mongo_colletion):
    """returns a list of items from a mongo collection"""
    return [school for school in mongo_colletion.find()]

#!/usr/bin/env python3

# 11-schools_by_topics.py

"""filters a mongo collection"""


def schools_by_topic(mongo_collection, topic: str) -> list:
    """Filters a mongo collection accroding to topic returns a list of documents"""
    schools = [school for school in mongo_collection.find(
    ) if topic in school.get('topics', '')]
    return schools

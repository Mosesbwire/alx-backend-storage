#!/usr/bin/env python3

# 10-update_topics.py

"""update data in a mongo collection"""


def update_topics(mongo_collection, name: str, topics: list[str]) -> None:
    """updates data of document with given name arg"""

    mongo_collection.find_one_and_update(
        {"name": name}, {'$set': {'topics': topics}})

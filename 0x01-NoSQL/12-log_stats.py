#!/usr/bin/env python3
# 12-log_stats.py

"""Provide statistcs of an nginx server"""

from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")

logs_collection = client.logs.nginx

num_of_logs = logs_collection.count_documents({})

print(f"{num_of_logs} logs")

methods = {
    "GET": 0,
    "POST": 0,
    "PUT": 0,
    "PATCH": 0,
    "DELETE": 0
}

status_path = 0

for req in logs_collection.find():
    if req["method"] == "GET":
        methods["GET"] += 1

    if req["method"] == "POST":
        methods["POST"] += 1

    if req["method"] == "PUT":
        methods["PUT"] += 1

    if req["method"] == "PATCH":
        methods["PATCH"] += 1

    if req["method"] == "DELETE":
        methods["DELETE"] += 1

    if req["path"] == "/status":
        status_path += 1

print("Methods:")

for key, val in methods.items():
    print(f'\tmethod {key}: {val}')

print(f"{status_path} status check")

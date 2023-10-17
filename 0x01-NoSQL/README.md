## NoSQL Database - MongoDb

## What NoSQL means

NoSQL stands for "Not Only SQL". It is a term used to describe a wide range of database technologies that do not use the traditional relational SQL database model. NoSQL databases are often designed to be more scalable and flexible than relational databases, and they can be used to store a variety of different data types, including documents, graphs, and key-value pairs.

## What is the difference between SQL and NoSQL?

SQL databases use a relational model to store data. This model organizes data into tables, which are made up of rows and columns. Each row represents a single record, and each column represents a different attribute of that record. SQL databases use a structured query language (SQL) to query and manipulate data.

NoSQL databases do not use a relational model to store data. Instead, they use a variety of different data models, such as document, graph, and key-value models. NoSQL databases often use a variety of different query languages, such as JSON query language (JQL) and MongoDB query language (MQL).

## What is ACID?

ACID stands for Atomicity, Consistency, Isolation, and Durability. It is a set of properties that are important for database transactions.

* **Atomicity:** A transaction is atomic if it is either completed successfully or not completed at all.
* **Consistency:** A transaction is consistent if it maintains the integrity of the database.
* **Isolation:** A transaction is isolated from other transactions so that it cannot be affected by them.
* **Durability:** A transaction is durable if its changes are permanent and cannot be lost.

## What is a document store?

A document store is a type of NoSQL database that stores data in documents. Documents are typically JSON or XML objects that contain a variety of different data types. Document stores are often used to store semi-structured data, such as web pages and social media posts.

## What are NoSQL types?

There are four main types of NoSQL databases:

* **Document databases:** Document databases store data in documents. Documents are typically JSON or XML objects that contain a variety of different data types.
* **Graph databases:** Graph databases store data in nodes and edges. Nodes represent entities, and edges represent relationships between entities. Graph databases are often used to store social networks and other types of connected data.
* **Key-value databases:** Key-value databases store data in key-value pairs. Keys are unique identifiers, and values can be any type of data. Key-value databases are often used to store cache data and other types of frequently accessed data.
* **Wide-column databases:** Wide-column databases store data in columns. Each column can store a different data type. Wide-column databases are often used to store large amounts of data that needs to be queried quickly.

## What are the benefits of a NoSQL database?

NoSQL databases offer a number of benefits over relational databases, including:

* **Scalability:** NoSQL databases are designed to be scalable, meaning that they can handle large amounts of data and traffic.
* **Flexibility:** NoSQL databases are flexible, meaning that they can store a variety of different data types and support a variety of different use cases.
* **Performance:** NoSQL databases can often offer better performance than relational databases for certain types of queries.

## How to query information from a NoSQL database

The specific way to query information from a NoSQL database depends on the type of NoSQL database you are using. However, most NoSQL databases support a variety of different query languages, such as JSON query language (JQL) and MongoDB query language (MQL).

## How to insert/update/delete information from a NoSQL database

The specific way to insert/update/delete information from a NoSQL database depends on the type of NoSQL database you are using. However, most NoSQL databases support a variety of different operations, such as `insert()`, `update()`, and `delete()`.

## How to use MongoDB

MongoDB is a popular NoSQL database that uses a document model to store data. MongoDB is known for its scalability and flexibility.

To use MongoDB, you will need to install the MongoDB server and client. Once you have installed MongoDB, you can create a new database and collection using the following commands:

```mongo
use my_database
db.createCollection("my_collection")
```

To perform CRUD operations in MongoDB, you can use the following commands:

* **Create:** To create a new document, you can use the `insertOne()` or `insertMany()` methods.
* **Read:** To read a document, you can use the `findOne()` or `find()` methods.
* **Update:** To update a document, you can use the `updateOne()` or `updateMany()` methods.
* **Delete:** To delete a document, you can use the `deleteOne()` or `deleteMany()` methods.

## How to use PyMongo

PyMongo is the official MongoDB Python driver. It provides a Pythonic interface for interacting with MongoDB databases.

### Installation

To use PyMongo, you will first need to install it. You can do this using pip:

`pip install pymongo`

### Usage

Once PyMongo is installed, you can start using it to connect to a MongoDB database:

```python
from pymongo import MongoClient

# Connect to the MongoDB database hon host
client = MongoClient("mongodb://127.0.0.1:27017")

# Get the database
db = client["my_database"]

# Get the collection
collection = db["my_collection"]
```
### Create
```python
# Create a new document
collection.insert_one({"name": "cli254", "age": 25})

# Create multiple documents
collection.insert_many([{"name": "cli254", "age": 25}, {"name": "bz254", "age": 20}])
```

### Read
```python
# Find a single document
document = collection.find_one({"name": "cli254"})

# Find all documents in the collection
cursor = collection.find()

# Iterate over the documents
for document in cursor:
    print(document)

```

### Update
```python
# Update a single document
collection.find_one_and_update({"name": "cli254"}, {"$set": {"age": 40}})

```

### Delete
```python
# Delete a single document
collection.delete_one({"name": "bz254"})
```

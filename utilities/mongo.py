import re

from pymongo import MongoClient

from decouple import config

# connect to MongoDB cluster
cluster = MongoClient(config('MONGO_DB_URL'))

db = cluster['discord']
collection = db['search']


def post_to_mongo_db(data):
    collection.insert_one(data)


def fetch_from_mongo_db(query):
    regx = re.compile(f"{query}", re.IGNORECASE)
    return collection.find({"query": regx}).distinct("query")

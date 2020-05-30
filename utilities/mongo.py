import re

from pymongo import MongoClient

from decouple import config

# connect to MongoDB cluster
cluster = MongoClient(config('MONGO_DB_URL'))

# db name is discord
db = cluster['discord']

# collection in the db is of name search
collection = db['search']


def post_to_mongo_db(data):     # function pushes a row in collection search
    collection.insert_one(data)


def fetch_from_mongo_db(query):     # function fetches distinct queries from history which matches pattern of query
    regx = re.compile(f"{query}", re.IGNORECASE)
    return collection.find({"query": regx}).distinct("query")

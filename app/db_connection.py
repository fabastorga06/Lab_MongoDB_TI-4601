import pymongo

_client = pymongo.MongoClient("mongodb://localhost:27017/")
_database = _client["LAB_DB"]
_movies = _database["movies"]

_query = { "country": "USA" }

_docs = _movies.find(_query)

for doc in _docs:
  print (doc["name"]) 
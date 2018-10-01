# coding=utf-8
import pymongo
from queries import *

_client = pymongo.MongoClient("mongodb://localhost:27017/")
_database = _client["LAB_DB"]

query1 = movie_info(_database, "Amélie")

print "-----------------------------------------------------"

query2 = movies_franchise(_database, "Rocky Franchise")



# coding=utf-8
import pymongo
from queries import *

_client = pymongo.MongoClient("mongodb://localhost:27017/")
_database = _client["LAB_DB"]

#  Queries  #

query1 = movie_info(_database, "Amélie")
query2 = movies_franchise(_database, "Rocky Franchise")
query3 = movies_in_range(_database, 2000, 2010)
query4 = movies_per_producer(_database, "DreamWorks")

#query 5
amt_movies = amount_movies(_database)
less_duration = less_duration_movie(_database)
higher_duration = higher_duration_movie(_database)
avg_duration = average_duration_movie(_database)

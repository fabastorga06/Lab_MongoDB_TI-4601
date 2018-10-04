# coding=utf-8
from db_connection import *
from queries import *

# Stablish connection with the database #
_database = database_connection()


#--------------------------------------------------------------#
#  Queries  #
#query1 = movie_info(_database, "aaaa")
#print query1
#query2 = movies_franchise(_database, "Rocky Franchise")
#query3 = movies_in_range(_database, 2000, 2010)
#query4 = movies_per_producer(_database, "DreamWorks")

#query 5
#amt_movies = amount_movies(_database)
#less_duration = less_duration_movie(_database)
#higher_duration = higher_duration_movie(_database)
#avg_duration = average_duration_movie(_database)
#--------------------------------------------------------------#

# Control data flush among user interface and database #
def movie_data_request(ptitle):
    return ( movie_info(_database, ptitle) )
    
def movies_franchise_request(pfranchise):
    return ( movies_franchise(_database, pfranchise) ) 

def years_movies_request(pstart, pfinal):
    return ( movies_in_range(_database, pstart, pfinal) )

def producer_movies_request(pproducer):
    return ( movies_per_producer(_database, pproducer) )

def less_movie_request():
    _movie = less_duration_movie(_database)
    return _movie[0]["name"]

def high_movie_request():
    _movie = higher_duration_movie(_database)
    return _movie[0]["name"]

def amount_movies_request():
    return str(amount_movies(_database))

def producer_averages_request():
    _avgs = average_duration_movie(_database)
    return _avgs
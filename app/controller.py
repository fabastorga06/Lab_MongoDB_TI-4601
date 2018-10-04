# coding=utf-8
from db_connection import *
from queries import *

# Stablish connection with the database #
_database = database_connection()

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
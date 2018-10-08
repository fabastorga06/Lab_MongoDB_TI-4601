#################################  QUERIES #############################################
import pymongo

# Returns specific movie information #
def movie_info(pdb, pmovie):
    _list = []
    _list.append( pdb["movies"].find_one( {"name":pmovie} ) )
    return _list
# Returns movies information according to franchise #
def movies_franchise(pdb, pfranchise):
    _movies = pdb["movies"]
    _filter = { "franchise":pfranchise }
    _docs = _movies.find( _filter )
    return ( list(_docs) )

#Returns movies in specific date range
def movies_in_range(pdb, pinitdate, pfinaldate):
    _movies = pdb["movies"]
    _filter = { "$and": [{"year":{"$gte":pinitdate}}, {"year":{"$lte":pfinaldate}}] }
    _docs = _movies.find( _filter )
    return ( list(_docs) )

# Returns movies according to producer 
def movies_per_producer(pdb, pproducer):   
    movies_producer = pdb["movies"].aggregate (
        [{"$match" : { "company" : pproducer }},
        {"$project" : { "_id":0, "name":1, "genre":1, "year":1 }}
	])	
    return ( list(movies_producer) )

# Return the amount of movies in the database
def amount_movies(pdb):
    return pdb["movies"].find().count()

# Returns an specific movie with the less duration
def less_duration_movie(pdb):
    less = pdb["movies"].aggregate (
        [
            { "$sort" : {"duration": 1} },
            { "$limit" : 1 }
        ]
    )
    return ( list(less) )

# Returns an specific movie with the higher duration
def higher_duration_movie(pdb):
    high = pdb["movies"].aggregate (
        [
            { "$sort" : {"duration": -1} },
            { "$limit" : 1 }
        ]
    )
    return ( list(high) )

# Returns the average duration among all movies in database 
def average_duration_movie(pdb):
    averages_per_producer = pdb["movies"].aggregate(
        [
            {
            "$group":
                {
                "_id": "$company",
                "average": { "$avg": "$duration" }
                }
            }
        ]
    )
    return ( list(averages_per_producer) )


#Insert new document in some collection of the database 
def insert_new_doc(pdb, pdoc, pcollection):
    _collection = pdb[pcollection]
    if '_id' in pdoc: 
        del pdoc['_id'] 
    _collection.insert_one(pdoc)


def ask_data(pdb, pcollection, pkey):
    return list( pdb[pcollection].find( {}, {pkey:1} ) ) 

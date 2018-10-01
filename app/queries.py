 
# Returns specific movie information #
def movie_info(pdb, pmovie):
    return pdb["movies"].find_one( {"name":pmovie} )

# Returns movies information according to franchise #
def movies_franchise(pdb, pfranchise):
    _movies = pdb["movies"]
    _filter = {"franchise":pfranchise}
    _docs = _movies.find( _filter )
   # for doc in _docs:
   #     print (doc["name"])
    return _docs


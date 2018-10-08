###############     SET DATABASE CONNECTION     ######################################
import pymongo

def database_connection():
    try:
        _client = pymongo.MongoClient("mongodb://localhost:27017/")
        _db = _client["LAB_DB"]
        print ("Connecting database...")
        print ("Connected!")
        return _db
    except:
        print ("Coudn't connect to database")
from pymongo import MongoClient

# Need to create this for app.py, can call in the function
mongo_url = "mongodb://localhost:27017/"

db_name = "SFILS"
col_name = "LibraryUsage"

def get_collection():
    client = MongoClient(mongo_url)
    db = client[db_name]
    return db[col_name]
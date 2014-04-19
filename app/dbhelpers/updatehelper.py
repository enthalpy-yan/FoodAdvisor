import json
from pymongo import MongoClient

def update_collection(db_name, collection_name):
    client = MongoClient('localhost', 27017)
    db = client[db_name]
    collection = db[collection_name]
    cursor = collection.find()
    for item in cursor:
        image_id = item['_id']
        description = item['description'].split()
        collection.update(
            {'_id': image_id}, 
            {'$set': {'description_search': description}},
            upsert=False
        )

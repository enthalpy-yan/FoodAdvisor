"""
script for update DB, add new field description_search.
"""

from pymongo import MongoClient

def update_collection(db_name, collection_name):
    """
    Update image collections with new field, description_search.
    
    Parameter:
        db_name: database name
        collection_name: collection name
    """
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

def create_indexes(db_name, collection_name):
    """
    Create full text indexes with name and description fields
    """
    client = MongoClient('localhost', 27017)
    db = client[db_name]
    collection = db[collection_name]
    collection.create_index([
        ('description', 'text'),
        ('business_info.name', 'text')
    ])

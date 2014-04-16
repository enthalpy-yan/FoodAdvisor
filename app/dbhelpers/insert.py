"""
Module for insert image data into local MongoDB.
"""
import json
from pymongo import MongoClient

def insertImages(json_file, db_name, collection_name):
    """
    Populate data from json files.

    Parameter
    ---------
    json_file: images informations json file.
    db_name: database name.
    collection_name: collection name.
    """
    client = MongoClient('localhost', 27017)
    with open(json_file) as inputfile:
        images_json = json.load(inputfile)
    db = client[db_name]
    collection = db[collection_name]
    collection.remove()
    for img in images_json:
        collection.insert(img)


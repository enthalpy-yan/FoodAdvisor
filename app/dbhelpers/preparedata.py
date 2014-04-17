#!/usr/bin/env python

"""
Script for inserting data into database.
"""

from inserthelper import insert_images

if __name__ == '__main__':
    insert_images('../outputs/images_data.txt', 'FoodAdvisor', 'images')

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline =

def aggregate(db, pipeline):
    result = db.cities.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('FoodAdvisor')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    assert len(result["result"]) == 1
    assert result["result"][0]["avg"] == 196025.97814809752
    import pprint
    pprint.pprint(result)

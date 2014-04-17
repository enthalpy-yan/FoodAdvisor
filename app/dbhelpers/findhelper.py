"""
Module for database queries.
"""

def find_one_image(db):
    return db.images.find_one()

def find_all_images(db, mylimit=20):
    return db.images.find().limit(mylimit)

def find_image_by_aggregation(db, pipeline):
    return db.images.aggregate(pipeline)['result']

def find_image_by_id(db, image_ids):
    pipeline = [{'$match': {'image_id': {'$in': image_ids}}},
                {'$limit': 20}]
    return find_image_by_aggregation(db, pipeline)

def find_image_by_text(db, keywords):
    pipeline = [{'$match': {'$text': {'$search': keywords}}},
                {'$limit': 50}]
    return find_image_by_aggregation(db, pipeline)

"""
Module for database queries.
"""
import re

def _raw_string(s):
    if isinstance(s, str):
        s = s.encode('string-escape')
    elif isinstance(s, unicode):
        s = s.encode('unicode-escape')
    return s

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

def text_suggestion(db, term):
    """
    Suggest sentence with the given term.

    Parameter
    ---------
    db: MongoDB instance.
    term: prefix string used to given suggestion.

    Return
    ------
    A suggestion list extracting from name and description field.
    """
    raw_string_pattern = _raw_string('^' + term)
    pattern = re.compile(raw_string_pattern, re.IGNORECASE)
    pipeline_dspt = [{'$match': {'description': {'$regex': pattern,
                                                 '$options': 'i'}}},
                     {'$sort': {'rating': -1}},
                     {'$limit': 15}]
    pipeline_name = [{'$match': {'business_info.name': {'$regex': pattern,
                                          '$options': 'i'}}},
                     {'$sort': {'rating': -1}},
                     {'$limit': 15}]
    result_dspt = find_image_by_aggregation(db, pipeline_dspt)
    result_name = find_image_by_aggregation(db, pipeline_name)
    suggestion = set()
    if result_dspt:
        for r in result_dspt:
            suggestion.add(r['description'])
    if result_name:
        for r in result_name:
            suggestion.add(r['business_info']['name'])
    return suggestion

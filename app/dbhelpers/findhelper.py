"""
Module for database queries.
"""
import re
from nltk.corpus import stopwords

CACHEDSTOPWORDS = stopwords.words("english")

def _raw_string(s):
    if isinstance(s, str):
        s = s.encode('string-escape')
    elif isinstance(s, unicode):
        s = s.encode('unicode-escape')
    return s

def find_one_image(db):
    return db.images.find_one()

def find_test(db):
    return [db.images.find_one({'image_id': 13000}),
            db.images.find_one({'image_id': 8291}),
            db.images.find_one({'image_id': 200}),
            db.images.find_one({'image_id': 593}),
            db.images.find_one({'image_id': 14000}),
            db.images.find_one({'image_id': 15131}),
            db.images.find_one({'image_id': 6718}),
            db.images.find_one({'image_id': 2437}),
            db.images.find_one({'image_id': 9000})]

def find_all_images(db, mylimit=20):
    return db.images.find().limit(mylimit)

def find_image_by_aggregation(db, pipeline):
    return db.images.aggregate(pipeline)['result']

def find_image_by_id(db, image_ids, offset=12):
    pipeline = [{'$match': {'image_id': {'$in': image_ids}}},
                {'$limit': offset}]
    return find_image_by_aggregation(db, pipeline)

def find_image_by_text(db, keywords, offset=12):
    pipeline = [{'$match': {'$text': {'$search': keywords}}},
                {'$limit': offset}]
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
    pipeline_dspt = [{'$project': {'des': '$description_search'}},
                     {'$unwind': '$des'},
                     {'$match': {'des': {'$regex': pattern,
                                         '$options': 'i'}}},
                     {'$sort': {'rating': -1}},
                     {'$limit': 100}]
    pipeline_name = [{'$match': {'business_info.name': {'$regex': pattern,
                                          '$options': 'i'}}},
                     {'$sort': {'rating': -1}},
                     {'$limit': 15}]
    pipeline_category = [{'$project': {'category': '$business_info.category'}},
                         {'$unwind': '$category'},
                         {'$match': {'category': {'$regex': pattern,
                                                  '$options': 'i'}}},
                         {'$sort': {'rating': -1}},
                         {'$limit': 15}]
    result_dspt = find_image_by_aggregation(db, pipeline_dspt)
    result_name = find_image_by_aggregation(db, pipeline_name)
    result_cat = find_image_by_aggregation(db, pipeline_category)
    suggestion = set()
    if result_dspt:
        for r in result_dspt:
            if r['des'] not in CACHEDSTOPWORDS:
                suggestion.add(r['des'])
    if result_name:
        for r in result_name:
            suggestion.add(r['business_info']['name'])
    if result_cat:
        for r in result_cat:
            for c in r['category']:
                suggestion.add(c)
    ret = [{'suggestion': s} for s in suggestion]
    return {'results': ret[:15]}

def sort_text_by_rating(db, keywords, offset):
    pipeline = [{'$match': {'$text': {'$search': keywords}}},
                {'$sort': {'business_info.rating': -1}},
                {'$limit': offset}]
    return find_image_by_aggregation(db, pipeline)

def sort_text_by_name(db, keywords, offset):
    pipeline = [{'$match': {'$text': {'$search': keywords}}},
                {'$sort': {'business_info.name': 1}},
                {'$limit': offset}]
    return find_image_by_aggregation(db, pipeline)

def sort_image_by_rating(db, image_ids, offset):
    pipeline = [{'$match': {'image_id': {'$in': image_ids}}},
                {'$sort': {'business_info.rating': -1}},
                {'$limit': offset}]
    return find_image_by_aggregation(db, pipeline)

def sort_image_by_name(db, image_ids, offset):
    pipeline = [{'$match': {'image_id': {'$in': image_ids}}},
                {'$sort': {'business_info.name': 1}},
                {'$limit': offset}]
    return find_image_by_aggregation(db, pipeline)

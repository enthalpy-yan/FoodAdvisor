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
                     {'$group': {'_id': '$des', 'sum': {'$sum': 1}}},
                     {'$match': {'_id': {'$regex': pattern,
                                         '$options': 'i'}}},
                     {'$sort': {'sum': -1}},
                     {'$limit': 15}]
    # pipeline_name = [{'$match': {'business_info.name': {'$regex': pattern,
    #                                       '$options': 'i'}}},
    #                  {'$sort': {'rating': -1}},
    #                  {'$limit': 15}]
    dspt_suggestion = find_image_by_aggregation(db, pipeline_dspt)
    trimed_suggestion = [doc for doc in dspt_suggestion
                         if doc['_id'].lower() not in CACHEDSTOPWORDS]
    return {'results': trimed_suggestion}

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

def find_image_by_id_new(db, image_id):
    pipeline = [{'$match': {'image_id': image_id}}]
    return find_image_by_aggregation(db, pipeline)

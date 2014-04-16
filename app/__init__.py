from flask import current_app
from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__, static_url_path='')
app.config.from_object('config')

# upload image configuration
app.config['UPLOAD_FOLDER'] = 'app/outputs/imgqueries/'
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#DB name configuration.
app.config['MONGO_DBNAME'] = 'test'
mongo = PyMongo(app, config_prefix='MONGO')

#Set app context global variable
ctx = app.app_context()
ctx.push()
current_app.mycreate = "ajlknl123j1l2k3jn123jnansfkajwe"

# Fake DB data
current_app.business = 
{
    {
        'image_id': 101
        'description': "one hundred and one",
        'relpath': "static/images/101.jpg",
        'business_id': "chinese-food-hoboken",
        'business_info': {
            'name': "yeung two",
            'rating': 4.0,
            'phone_number': "＋1-201－420－7197",
            'review_count': 298,
            'location': {
                'display_name': "Yeung 2",
                'details':{
                    'longitude': 40.750792,
                    'latitude': -74.027127,
                }
            }
            'category': [
                "Chinese food",
                "Sushi",
                "Japanese staples"
            ]
        }
    },
    {
        'image_id': 340
        'description': "three hundred and fourty",
        'relpath': "static/images/340.jpg",
        'business_id': "Ramen-new-york",
        'business_info': {
            'name': "Ramen store",
            'rating': 4.5,
            'phone_number': "＋1-631－420－7197",
            'review_count': 4362,
            'location': {
                'display_name': "Ramen store",
                'details':{
                    'longitude': 40.7466955,
                    'latitude': -74.0045213,
                }
            }
            'category': [
                "local food",
                "Ramen",
                "Japanese staples"
            ]
        }
    },
    {
        'image_id': 9001
        'description': "nine thousands and one",
        'relpath': "static/images/9001.jpg",
        'business_id': "italy-new-york",
        'business_info': {
            'name': "italian food",
            'rating': 3.5,
            'phone_number': "＋1-631－254－4525",
            'review_count': 157,
            'location': {
                'display_name': "Italian",
                'details':{
                    'longitude': 40.7384217,
                    'latitude': -74.0014305,
                }
            }
            'category': [
                "italian food",
                "europe",
                "Pizza",
                "pub"
            ]
        }
    }    
}
from app.routes import index
from app.restapis import api


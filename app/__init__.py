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
# current_app.business = {
#     'image_id': 101
#     'description': "",
#     'relpath': "images/dir/ .jpg",
#     'business_id': ,
#     'business_info': {
#         'name': (from Yelp API),
#         'rating': (from Yelp API),
#         'phone_number': (from Yelp API),
#         'review_count': (from Yelp API),
#         'location': {
#             'displayname': (from Yelp API),
#             'details':{
#                 'longitude': (Google Geo code API),
#                 'latitude': (Google Geo code API),
#             }
#         }
#         'category': (from Yelp API)
#     }
# }

from app.routes import index
from app.restapis import api


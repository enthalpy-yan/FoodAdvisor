from flask import current_app
from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__, static_url_path='')
app.config.from_object('config')

# upload image configuration
app.config['UPLOAD_FOLDER'] = 'app/outputs/imgqueries/'
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#DB name configuration.
app.config['MONGO_DBNAME'] = 'FoodAdvisor'
mongo = PyMongo(app, config_prefix='MONGO')

#Set app context global variable
ctx = app.app_context()
ctx.push()
current_app.mycreate = "ajlknl123j1l2k3jn123jnansfkajwe"

# Fake DB data
current_app.images = [
    {
        "business_info": {
            "category": [
                [
                    "Indian",
                    "indpak"
                ],
                [
                    "Mexican",
                    "mexican"
                ],
                [
                    "American (New)",
                    "newamerican"
                ]
            ],
            "rating": 4.0,
            "review_count": 178,
            "name": "23rd Street Cafe",
            "phone": "+1-213-749-1593",
            "location": {
                "display_name": [
                    "936 W 23rd St",
                    "University Park",
                    "Los Angeles, CA 90007"
                ],
                "details": {
                    "latitude": 34.033785,
                    "longitude": -118.2808464
                }
            }
        },
        "description": "Amazing chicken tikka and aloo tacos",
        "abspath": "/Users/hanyan/Desktop/Homework/CS598/FoodAdvisor/app/static/images/foods/23rd-street-cafe-los-angeles/Amazing chicken tikka and aloo tacos.jpg",
        "business_id": "23rd-street-cafe-los-angeles",
        "image_id": 0,
        "relpath": "images/foods/23rd-street-cafe-los-angeles/Amazing chicken tikka and aloo tacos.jpg"
    },
    {
        "business_info": {
            "category": [
                [
                    "Indian",
                    "indpak"
                ],
                [
                    "Mexican",
                    "mexican"
                ],
                [
                    "American (New)",
                    "newamerican"
                ]
            ],
            "rating": 4.0,
            "review_count": 178,
            "name": "23rd Street Cafe",
            "phone": "+1-213-749-1593",
            "location": {
                "display_name": [
                    "936 W 23rd St",
                    "University Park",
                    "Los Angeles, CA 90007"
                ],
                "details": {
                    "latitude": 34.033785,
                    "longitude": -118.2808464
                }
            }
        },
        "description": "Asada and Eggs with Hash Browns",
        "abspath": "/Users/hanyan/Desktop/Homework/CS598/FoodAdvisor/app/static/images/foods/23rd-street-cafe-los-angeles/Asada and Eggs with Hash Browns.jpg",
        "business_id": "23rd-street-cafe-los-angeles",
        "image_id": 1,
        "relpath": "images/foods/23rd-street-cafe-los-angeles/Asada and Eggs with Hash Browns.jpg"
    },
    {
        "business_info": {
            "category": [
                [
                    "Indian",
                    "indpak"
                ],
                [
                    "Mexican",
                    "mexican"
                ],
                [
                    "American (New)",
                    "newamerican"
                ]
            ],
            "rating": 4.0,
            "review_count": 178,
            "name": "23rd Street Cafe",
            "phone": "+1-213-749-1593",
            "location": {
                "display_name": [
                    "936 W 23rd St",
                    "University Park",
                    "Los Angeles, CA 90007"
                ],
                "details": {
                    "latitude": 34.033785,
                    "longitude": -118.2808464
                }
            }
        },
        "description": "Breakfast Burrito with Sausage",
        "abspath": "/Users/hanyan/Desktop/Homework/CS598/FoodAdvisor/app/static/images/foods/23rd-street-cafe-los-angeles/Breakfast Burrito with Sausage.jpg",
        "business_id": "23rd-street-cafe-los-angeles",
        "image_id": 2,
        "relpath": "images/foods/23rd-street-cafe-los-angeles/Breakfast Burrito with Sausage.jpg"
    }
]
from app.routes import index
from app.restapis import api


from flask import current_app
from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.restful import Api
import numpy as np

app = Flask(__name__, static_url_path='')
app.config.from_object('config')

restapi = Api(app)

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
codebook = np.loadtxt('app/outputs/codebook.txt')
tfidf = np.loadtxt('app/outputs/tfidf.txt')
current_app.codebook = codebook
current_app.tfidf = tfidf

from app.routes import index
from app.restapis import api

restapi.add_resource(api.UpLoad, '/api/foodimages/search')
restapi.add_resource(api.Suggestion, '/api/foodtexts/search')


from flask import current_app
from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__, static_url_path='')
app.config.from_object('config')

#DB name configuration.
app.config['MONGO_DBNAME'] = 'test'
mongo = PyMongo(app, config_prefix='MONGO')

#Set app context global variable
ctx = app.app_context()
ctx.push()
current_app.mycreate = "ajlknl123j1l2k3jn123jnansfkajwe"

from app.routes import index
from app.restapis import api


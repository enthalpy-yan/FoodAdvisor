from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__, static_url_path='')
app.config.from_object('config')

#DB name configuration.
app.config['MONGO_DBNAME'] = 'test'
mongo = PyMongo(app, config_prefix='MONGO')

from app.routes import index
from app.restapis import api

from app import app
from app import mongo
from flask import Response
from bson import json_util

@app.route('/test')
def test():
    myname = mongo.db.users.find_one()
    return Response(
        json_util.dumps(myname),
        mimetype='application/json'
    mage)

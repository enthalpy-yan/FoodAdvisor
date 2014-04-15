from app import app
from app import mongo
from flask import Response
from flask import current_app
from bson import json_util

@app.route('/test')
def test():
    myname = mongo.db.users.find_one()
    return Response(
        json_util.dumps(current_app.mycreate),
        mimetype='application/json'
    )

import os
from app import app
from app import mongo
from flask import Response, request, current_app
from bson import json_util
from werkzeug import secure_filename
from app.apphelpers import upload
from app.dbhelpers import findhelper

@app.route('/test')
def test():
    images = findhelper.find_test(mongo.db)
    return Response(
        json_util.dumps(images),
        mimetype='application/json'
    )

@app.route('/api/foodtexts/search', methods=['GET'])
def suggestion():
    """
    Get word suggestion with the given term.
    """
    term = request.args.get('term')
    suggestion_list = findhelper.text_suggestion(mongo.db, term)
    return Response(
        json_util.dumps(suggestion_list),
        mimetype='application/json'
    )

# Route that will process the file upload
@app.route('/api/foodimages/search', methods=['POST'])
def search():
    # Get the name of the uploaded file
    file = request.files['uploadFile']

    print

    if file and upload.allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return Response(
            json_util.dumps(app.config['UPLOAD_FOLDER'] + filename),
            mimetype='application/json'
        )

import os
from app import app
from app import mongo
from flask import Response, request, current_app
from bson import json_util
from werkzeug import secure_filename
from app.apphelpers import upload

@app.route('/test')
def test():
    myname = mongo.db.users.find_one()
    return Response(
        json_util.dumps(current_app.mycreate),
        mimetype='application/json'
    )

# Route that will process the file upload
@app.route('/foodimages/search', methods=['POST'])
def search():
    # Get the name of the uploaded file
    file = request.files['imgfile']
    
    if file and upload.allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return Response(
            json_util.dumps(app.config['UPLOAD_FOLDER'] + filename),
            mimetype='application/json'
        )
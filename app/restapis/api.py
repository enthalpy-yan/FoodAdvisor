import os
from app import app
from app import mongo
from flask import Response, request, current_app
from bson import json_util
from werkzeug import secure_filename
from app.apphelpers import upload
from app.dbhelpers import findhelper
from flask.ext.restful import Api, Resource, reqparse


@app.route('/test')
def test():
    images = findhelper.find_all_images(mongo.db)
    return Response(
        json_util.dumps(images),
        mimetype='application/json'
    )

class Suggestion(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('term', type=str)
        super(Suggestion, self).__init__()

    def get(self):
        args = self.reqparse.parse_args()
        term = args['term']
        suggestion_list = findhelper.text_suggestion(mongo.db, term)
        return Response(
            json_util.dumps(suggestion_list),
            mimetype='application/json'
        )

# Route that will process the file upload

class UpLoad(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('text', type=str)
        self.reqparse.add_argument('file', type=str)
        self.reqparse.add_argument('longitude', type=str)
        self.reqparse.add_argument('latitude', type=str)
        self.reqparse.add_argument('offset', type=str)
        self.reqparse.add_argument('query', type=str)
        self.reqparse.add_argument('sortbylocation', type=str)
        self.reqparse.add_argument('sortbyrating', type=str)
        self.reqparse.add_argument('sortbyname', type=str)
        super(UpLoad, self).__init__()

    def post(self):
        file = request.files['imgfile']
        if file and upload.allowed_file(file.filename):
            # filename = secure_filename(file.filename)

            filename = upload.generate_new_filename(file)
            savepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            abspath = os.path.join(os.path.abspath(''), savepath)
            file.save(abspath)

            # call search_by_image(indexmatrix, imagepath) to get images list
            imagesrst = [1, 3]

            businessinfo = findhelper.find_image_by_id(mongo.db, imagesrst)
            text = args['text']
            res = {
                'result': businessinfo,
                'status': { 'text': text, 'file': abspath }
            }
            
            return Response(
                json_util.dumps(res),
                mimetype='application/json'
            )

    def get(self):
        args = self.reqparse.parse_args()
        text = args['text']
        tt = findhelper.find_image_by_text(mongo.db, text)

        return Response(
            json_util.dumps(tt),
            mimetype='application/json'
        )
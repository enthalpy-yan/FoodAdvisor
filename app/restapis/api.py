import os
from app import app
from app import mongo
from flask import Response, request, current_app
from bson import json_util
from werkzeug import secure_filename
from app.apphelpers import upload
from app.dbhelpers import findhelper
from app.imagesearchapis import imagesearch
from flask.ext.restful import Api, Resource, reqparse


@app.route('/test')
def test():
    images = findhelper.find_test(mongo.db)
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
        self.reqparse.add_argument('file', type=str)
        self.reqparse.add_argument('offset', type=str)
        self.reqparse.add_argument('query', type=str)
        self.reqparse.add_argument('sortbyrating', type=str)
        self.reqparse.add_argument('sortbyname', type=str)
        super(UpLoad, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        file = request.files['uploadFile']
        if file and upload.allowed_file(file.filename):

            filename = upload.generate_new_filename(file)
            savepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            abspath = os.path.join(os.path.abspath(''), savepath)
            file.save(abspath)

            # call search_by_image(indexmatrix, imagepath) to get images list
            imagesrst = imagesearch.search_image(abspath,
                                     current_app.codebook,
                                     current_app.tfidf)

            businessinfo = findhelper.find_image_by_id(mongo.db, imagesrst, 12)

            # print businessinfo.__class__

            # query = args['query']
            # res = {
            #     'result': businessinfo,
            #     'status': { 'text': query, 'file': abspath }
            # }

            return Response(
                json_util.dumps(businessinfo),
                mimetype='application/json'
            )

    def get(self):
        args = self.reqparse.parse_args()
        abspath = args['file']
        query = args['query']
        offset = args['offset']

        if query and abspath is None:
            if args['sortbyrating']:
                querylist = findhelper.sort_text_by_rating(mongo.db, query, offset)
            elif args['sortbyname']:
                querylist = findhelper.sort_text_by_name(mongo.db, query, offset)
            else:
                querylist = findhelper.find_image_by_text(mongo.db, query, offset)

        elif abspath and query is None:
            
            imagesrst = imagesearch.search_image(abspath,
                                     current_app.codebook,
                                     current_app.tfidf)
            if args['sortbyrating']:
                querylist = findhelper.sort_image_by_rating(mongo.db, imagesrst, offset)
            elif args['sortbyname']:
                querylist = findhelper.sort_image_by_name(mongo.db, imagesrst, offset)
            else:
                querylist = findhelper.find_image_by_id(mongo.db, imagesrst, offset)

        res = {
            'result': querylist,
            'status': { 'text': query, 'file': abspath }
        }

        return Response(
            json_util.dumps(res),
            mimetype='application/json'
        )

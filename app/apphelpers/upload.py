from app import app
import os
import uuid
import itertools
from app.dbhelpers import findhelper

# Check if the file is one of the allowed types/extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def generate_new_filename(file):
    f, ext = os.path.splitext(file.filename)
    return str(uuid.uuid4().hex) + ext

def result_in_order(db, imagesrst,offset=12):
    result_list = []
    for x in xrange(offset):
        img = findhelper.find_image_by_id_new(db, imagesrst[x])
        result_list.append(img)
    return list(itertools.chain(*result_list))
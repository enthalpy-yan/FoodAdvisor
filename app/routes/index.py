from app import app
from flask import send_file

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serveIndex(path):
    return send_file('static/index.html')

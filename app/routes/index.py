from app import app
from flask import send_file

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serveIndex(path):
    return send_file('static/index.html')

from app import app

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/how')
def how():
    return app.send_static_file('index.html')

@app.route('/about')
def about():
    return app.send_static_file('index.html')

from app import app

# Check if the file is one of the allowed types/extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def generate_new_filename(file):
    f, ext = os.path.splitext(file.filename)
    return str(uuid.uuid4().hex) + ext
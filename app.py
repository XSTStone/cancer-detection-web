import os.path

from flask import Flask, request
from flask import render_template
from model import BreastCancer as Detector
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

HOSTNAME = 'sh-cynosdbmysql-grp-krdmzg9q.sql.tencentcdb.com'
PORT = 24711
USERNAME = 'root'
PASSWORD = 'Beyond2016'
DATABASE = 'CANCER_USER'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

db = SQLAlchemy(app)

with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))
        print(rs.fetchone())

base_dir = os.path.abspath(os.path.dirname(__file__)) + "/static/upload/img"

print(base_dir)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/detect/<path>')
def work(path=None):
    print(path)
    if path == 'my_image.jpg':
        path = 'model/my_image.jpg'
        print(path)
    else:
        print("No")
    Detector.work('detect', path)


@app.route('/upload-image', methods=['GET', 'POST'])
def get_image():
    img = request.files.get('image')
    basedir = os.path.abspath(os.path.dirname(__file__))
    path = basedir + "/static/img_detect/"
    img_name = img.filename
    file_path = path + img_name
    img.save(file_path)
    url = "/static/img_detect/" + img_name
    return url


@app.route('/test')
def test():
    return render_template("test.html")


@app.route('/uploader', methods=['GET', 'POST'])
def getImg():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
        f.save(os.path.join(base_dir, secure_filename(f.filename)))
        return "Success"
    else:
        return render_template("test.html")


if __name__ == '__main__':
    app.run()

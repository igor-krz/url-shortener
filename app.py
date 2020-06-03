from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import secrets
import os


# Initialise app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Config
# track modifications - warning messages don't appear when running
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3' + \
    os.path.join(basedir, 'db.sqlite3')

# Connect Database 
db = SQLAlchemy(app)

# Initialise marshmallow
ma = Marshmallow(app)

# Create Model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String)
    short_url = db.Column(db.String)

# Initialiser / Constructer (Pass in self and each fields)
    def __init__(self, long_url, short_url):
        self.long_url = long_url
        self.short_url = short_url


# Create Product Schema
class url_schema(ma.Schema):
    class Meta:
        fields = ('id', 'long_url', 'short_url')

# Init Schema
urls_schema = url_schema(many=True)
url_schema = url_schema()


# Generate secure tokens
def random_key():
    return secrets.token_urlsafe(12)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

# Route to Shorten URL
@app.route('/shorten', methods=['POST'])
def insert_url():
    url_original = request.form['content']
    url_key = random_key()
    new_url = URL(url_original, url_key)

    try:
        db.session.add(new_url)
        db.session.commit()
        return render_template('added.html', url=url_key)

    except:
        return 'ISSUE: link inserted cannot be added'

# Get ALL data  
@app.route('/all', methods=['GET'])
def get_all():
    all_urls = URL.query.all()
    result = urls_schema.dump(all_urls)
    return jsonify(result)

# Get Route for Key
@app.route('/<key>', methods=['GET'])
def get_url(key):
    product = URL.query.filter(URL.short_url == key).first().long_url
    return redirect(product)


if __name__ == '__main__':
    app.run(debug=True)
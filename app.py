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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')

# Connect Database 
db = SQLAlchemy(app)

# Initialise marshmallow
ma = Marshmallow(app)

# Create Model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longUrl = db.Column(db.String)
    shortUrl = db.Column(db.String)

# Initialiser / Constructer (Pass in self and each fields)
    def __init__(self, longUrl, shortUrl):
        self.longUrl = longUrl
        self.shortUrl = shortUrl


# Create Product Schema
class URLSchema(ma.Schema):
    class Meta:
        fields = ('id', 'longUrl', 'shortUrl')

# Init Schema
URLs_schema = URLSchema(many=True)
URL_schema = URLSchema()


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
    url_original = request.form["content"]
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
    result = URLs_schema.dump(all_urls)
    return jsonify(result)

# Get Route for Key
@app.route('/<key>', methods=['GET'])
def get_url(key):
    product = URL.query.filter(URL.shortUrl == key).first().longUrl
    return redirect(product)


if __name__ == '__main__':
    app.run(debug=True)
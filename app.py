from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
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

# Init ma
ma = Marshmallow(app)

# Create Model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longUrl = db.Column(db.String)
    shortUrl = db.Column(db.String)

# Pass in self and fields
    def __init__(self, longUrl, shortUrl):
        self.longUrl = longUrl
        self.shortUrl = shortUrl


# Create Product Schema
class URLSchema(ma.Schema):
    class Meta:
        fields = ('id', 'longUrl', 'shortUrl')

# Init Schema
URLs_schema = ProductSchema(many=True)
URL_schema = URLSchema()

# Routes
@app.route('/')
def index():
    return render_template('index.html')






if __name__ == '__main__':
    app.run(debug=True)
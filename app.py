from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialise app
app = Flask(__name__)


# Config
# track modifications - warning messages don't appear when running
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# Connect Database 
db = SQLAlchemy(app)

# Create Model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longUrl = db.Column(db.String)
    shortUrl = db.Column(db.String)sqlite3 db.sqlite3

# Routes
@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, make_response, render_template
import sqlite3

# initialise app
app = Flask(__name__)

# Database 
db = sqlite3.connect('database.db')
print('Opened database successfully')

db.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print ("Table created successfully")
db.close()

@app.route('/')
def home():
    return render_template ('index.html')


if __name__ == '__main__':
    app.run(debug=True)
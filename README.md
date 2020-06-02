# url-shortener

### Steps Checklist :
* Initialise App - Server 
* Setup Configs
* Connect Database
* Create Model
* Init Database
* Create Product Schema
* Init Product Schema
* Create Routes
* Create Templates
* Link Form to Routes - Methods[Post, Get]
* Create Test
* Create requirements.txt (freeze) 


### User stories
* User goes to homepage and inserts a long link
* User submits long URL
* URL data gets stored in database 
* Long URL gets converted to Short URL
* User receives the shortened URL link 


#### To RUN
* python3 -m venv env
* source env/bin/activate
* install sqlalchemy - pip install flask flask-sqlalchemy
* check dependencies - pip list
* to check DB  in terminal - sqlite3 db.sqlite3 / then .tables
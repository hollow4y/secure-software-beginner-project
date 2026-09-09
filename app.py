from flask import Flask, requestcurl.exe -X POST http://localhost:5000/login -d "username=shawn&password=test123"
from random import randint
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return f"User {username} created successfully"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return "successfully logged in :D"
    else:
        return "Invalid login credentials"


@app.route('/')
def home():
    text = "random number" + " " + str(randint(1,5))
    return text

@app.route('/home')
def homePage():
    return "welcome to the home page"

if __name__ == '__main__':
    app.run(debug=True)
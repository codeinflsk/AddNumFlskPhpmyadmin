from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY']='Secret Key'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:''@localhost/Addsum'
app.config['SQLALCHEMY_TRACK_NOTIFICATION'] = False

db = SQLAlchemy(app)

class Addition(db.Model):
   
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    num1 = db.Column(db.Integer)
    num2 = db.Column(db.Integer)
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        

    
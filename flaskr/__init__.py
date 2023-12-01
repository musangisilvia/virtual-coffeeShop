from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# configure db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:8QE1Oh8j9mPoruRmGtsw@database-1.creqgg4niwd7.eu-north-1.rds.amazonaws.com:3306/database-1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def login():
    return render_template('templates/index.html')



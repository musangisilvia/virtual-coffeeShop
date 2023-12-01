from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector


app = Flask(__name__)

# configure db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:8QE1Oh8j9mPoruRmGtsw@database-1.creqgg4niwd7.eu-north-1.rds.amazonaws.com:3306/VirtualCoffee'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/test-db-connection')
def test_db_connection():
    try:
        # Replace the values below with your actual database credentials
        connection = mysql.connector.connect(
            # :3306/VirtualCoffee
            host="database-1.creqgg4niwd7.eu-north-1.rds.amazonaws.com",
            user="admin",
            password="8QE1Oh8j9mPoruRmGtsw",
            database="VirtualCoffee"
        )

        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        result = cursor.fetchone()

        connection.close()

        return jsonify({"status": "success", "result": result[0]}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500



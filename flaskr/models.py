# models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import func, current_timestamp
# from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

class Users(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.current_timestamp())
    posts = relationship('Posts', back_populates='user')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
            return bcrypt.check_password_hash(self.password, password)
    

class Posts(db.Model):
    __tablename__ = "Posts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    user = relationship('Users', back_populates='posts')

    def __init__(self, user_id, content):
         self.user_id = user_id
         self.content = content

    def get_posts(self, user_id):
         posts = Posts.query.filter_by(user_id=user_id).all()
         return posts
    
    def get_all_posts():
         all_posts = Posts.query.order_by(Posts.created_at.desc()).all()
     #     print("=========\n",all_posts)
         return all_posts
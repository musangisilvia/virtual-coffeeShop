from flaskr import db
from sqlalchemy.sql.functions import func, current_timestamp

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.current_timestamp())

    def __repr__(self):
        return f'<User {self.username}>'



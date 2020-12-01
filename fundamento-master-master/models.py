from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(40))
    password = db.Column(db.String(80), nullable=False)

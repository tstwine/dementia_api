from flask_sqlalchemy import SQLAlchemy
from server import app
from datetime import datetime

db = SQLAlchemy(app)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    text = db.Column(db.Text)
    timeposted = db.Column(db.DateTime)

    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.timeposted = datetime.now()

    def __repr__(self):
        return '<Comment %r, %r, %r>' % (self.name, self.text, self.timeposted)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    timeposted = db.Column(db.DateTime)
    author = db.Column(db.String(80))

    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author
        self.timeposted = datetime.now()
from flask_sqlalchemy import SQLAlchemy
from server import app

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
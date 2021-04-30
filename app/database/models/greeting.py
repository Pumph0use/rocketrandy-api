from app.database.base import db


class Greeting(db.Model):
    __tablename__ = 'greetings'
    id = db.Column(db.Integer, primary_key=True)
    response = db.Column(db.String)
    added_by = db.Column(db.BigInteger, db.ForeignKey('users.id'))

    user = db.relationship('User')
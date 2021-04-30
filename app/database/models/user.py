from app.database.base import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=False)
    display_name = db.Column(db.String(32))
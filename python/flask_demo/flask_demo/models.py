from flask_demo import db
from hashlib import md5

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128), unique=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.password_encrypt(password)

    def __repr__(self):
        return '<User %r>' % self.username

    def password_encrypt(self, password):
        en_password = md5(password)
        return en_password.hexdigest()

    def is_active(self):
        return True

    def get_id(self):
        return unicode(id)

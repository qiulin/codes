from flask_demo import db
from flask_demo.utils import password_encrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password_encrypt(password)

    def __repr__(self):
        return '<User %r>' % self.username

    def is_active(self):
        return True

    def get_id(self):
        return unicode(id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey("User.id"))
    publish_datetime = db.Column(db.DateTime)
    title = db.Column(db.Text)
    markdown = db.Column(db.Text)
    html = db.Column(db.Text)

    def __init__(self, uid, publish_datetime, title, markdown):
        self.uid = uid
        self.publish_datetime = publish_datetime
        self.title = title
        self.markdown = markdown

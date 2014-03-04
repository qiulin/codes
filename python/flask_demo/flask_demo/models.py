from flask_demo import db
from hashlib import md5


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = User.password_encrypt(password)

    @staticmethod
    def user_validate(email, password):
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == User.password_encrypt(password):
                return user.id
        return None

    @staticmethod
    def password_encrypt(password):
        en_password = md5(password)
        return en_password.hexdigest()

    def __repr__(self):
        return '<User %r>' % self.username

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def is_authenticated(self):
        return True


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

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.fields.html5 import EmailField

class SignupForm(Form):
    username = StringField("Username", [validators.length(min=4, max=25), validators.required()])
    email = EmailField("Email", [validators.required(), validators.email()])
    password = PasswordField("Password", [validators.length(min=6, max=20), validators.required(),
                                          validators.equal_to('confirm', message="Passwords must match")])
    confirm = PasswordField("Repeat Password")
    submit = SubmitField("Signup")


class SigninForm(Form):
    email = EmailField("Email", [validators.required(), validators.email()])
    password = PasswordField("Password", [validators.length(min=6, max=20), validators.required()])
    submit = SubmitField("Signin")

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request, redirect, url_for

from flask_demo import app, db
from flask_demo.models import User
from flask_demo.forms import SignupForm, SigninForm
from flask_demo.utils import user_loader, user_validate

from flask.ext.login import login_user, login_required


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    #import pdb; pdb.set_trace()  # XXX BREAKPOINT
    form = SignupForm(request.form)
    error = None
    if request.method == "POST" and form.validate():
        user_old = User.query.filter_by(email=form.email.data).first()
        if not user_old:
            user = User(form.username.data, form.email.data, form.password.data)
        else:
            error = "This email has been used!"
            return render_template("signup.html", form=form, error=error)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index"))
    else:
        return render_template("signup.html", form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm(request.form)
    error = None
    if request.method=="POST" and form.validate():
        email = form.email.data
        password = form.password.data
        uid = user_validate(email, password)
        if uid:
            user = user_loader(uid)
            login_user(user)
            return redirect(url_for("profile"))
        else:
            error = "Email or Password was not correct."
            return render_template("signin.html", form=form, error=error)
    else:
        return render_template("signin.html", form=form)


@login_required
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template("profile.html")


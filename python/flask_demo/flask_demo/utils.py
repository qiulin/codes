#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashlib import md5
from flask_demo import login_manager
from flask_demo.models import User

@login_manager.user_loader
def user_loader(uid):
    # TODO: user_loader
    user = User.query.filter_by(id=uid).first()
    return user


def user_validate(email, password):
    user = User.query.filter_by(email=email).first()
    if user:
        if user.password == password_encrypt(password):
            return user.id
    return None


def password_encrypt(password):
    en_password = md5(password)
    return en_password.hexdigest()


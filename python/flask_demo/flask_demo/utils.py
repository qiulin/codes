#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_demo import login_manager
from flask_demo.models import User

@login_manager.user_loader
def user_loader(uid):
    user = User.query.filter_by(id=uid).first()
    return user

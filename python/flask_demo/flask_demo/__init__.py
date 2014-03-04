#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
doc

"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf.csrf import CsrfProtect
from flask.ext.login import LoginManager
import dev_config as config


__all__ = ['app', 'db', 'login_manager']


app = Flask(__name__)
app.config.from_object(config)
app.secret_key = app.config['SECRET_KEY']

db = SQLAlchemy(app)
CsrfProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)

from flask_demo import views
from flask_demo import models

login_manager.login_view = "signin"

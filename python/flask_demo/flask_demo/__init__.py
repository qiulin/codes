#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
doc

"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import dev_config as config


__all__ = ['app', 'db']


app = Flask(__name__)
app.config.from_object(config)
app.secret_key = app.config['SECRET_KEY']

db = SQLAlchemy(app)

from flask_demo import views
from flask_demo import models

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request, session, redirect, url_for, escape, flash

from flask_demo import app
from flask_demo.utils import *


@app.route("/")
def index():
    if 'username' in session:
        return "Logged in as %s" % escape(session['username'])
    return 'You are not logged in'


@app.route('/hello')
def hell():
    return "Hello World!"


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return "The project page"


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
           request.form['password'] != 'liqiulin':
            error = 'Invalid credentials'
        else:
            session['username'] = request.form['username']
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/tojson')
def xtojson():
    return render_template('tojson.html', msg='Hello World')


#@app.route('/upload', methods=['GET', 'POST'])
#def upload_file():
    #if request.method == 'POST':
        #f = request.files['the_file']
        #f.save('/root/work/python/' + secure_filename(f.filename))
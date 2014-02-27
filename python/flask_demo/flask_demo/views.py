#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request, session, redirect, url_for, escape, flash

from flask_demo import app
from flask_demo import utils


@app.route("/")
def index():
    return render_template('index.html')


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


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
           request.form['password'] != 'liqiulin':
            error = 'Invalid credentials'
        else:
            session['username'] = request.form['username']
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('signin.html', error=error)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    msg = None
#    if request.method == 'POST':
    #else:
#        render_template('signup.html', msg=msg)

@app.route('/tojson')
def xtojson():
    return render_template('tojson.html', msg='Hello World')



#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
doc

"""

from flask import Flask
from flask import render_template, request, session, redirect, url_for, escape


app = Flask(__name__)
app.secret_key = 'fjaeojfaojeoan3091u4jdsaou302r4jefaou0u0wqraofjef'

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
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        return render_template('login.html')


#@app.route('/upload', methods=['GET', 'POST'])
#def upload_file():
    #if request.method == 'POST':
        #f = request.files['the_file']
        #f.save('/root/work/python/' + secure_filename(f.filename))


def valid_login(username, password):
    return True


def log_the_user_in(username):
    pass


if __name__ == "__main__":
    app.run(debug=True)

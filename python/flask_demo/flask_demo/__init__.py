#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
doc

"""

from flask import Flask

app = Flask(__name__)
app.secret_key = 'fjaeojfaojeoan3091u4jdsaou302r4jefaou0u0wqraofjef'


from flask_demo import views


if __name__ == "__main__":
    app.run(debug=True)

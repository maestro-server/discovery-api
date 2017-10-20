# -*- encoding: utf-8 -*-
"""
Python Routes
Licence: GPLv3
"""

from app import app

@app.route("/")
def hello():
    return "Hello Worldd2!"
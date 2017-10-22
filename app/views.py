# -*- encoding: utf-8 -*-
"""
Python Routes
Licence: GPLv3
"""

from .models.control import Control
import datetime
from app import app

@app.route("/")
def main():
    return "Hello Worldd2!"

@app.route("/crawler/<datacenter>")
def info(datacenter):
    return "info %s" % datacenter

@app.route("/crawler/<datacenter>/full")
def full(datacenter):
    control = Control(datacenter)
    return control.full()

@app.route("/crawler/<datacenter>/parcial")
def parcial(datacenter):
    control = Control(datacenter)
    now = (datetime.datetime.now())
    return control.parcial(now)

@app.route("/crawler/<uuid:datacenter>/single/<instance_id>")
def single(datacenter, instance_id):
    control = Control(datacenter)
    return control.single(instance_id)
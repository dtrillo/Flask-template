from flask import Flask, render_template, url_for
from . import base

methods = ['GET', 'POST']
GET, POST = methods

nl = "\n"

@base.route('/')
def index():
	return render_template('blueprint.html')

from flask import request, redirect, render_template, url_for

from app import app

@app.route('/')
@app.route('/welcom')
def index():
	return render_template('welcome.html')

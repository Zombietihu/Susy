from flask import request, redirect, render_template, url_for, flash, Flask, session, abort
from app import app


@app.route('/')
def index():
	    return render_template('welcome.html')

@app.route('/home')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
	    return render_template('home.html')

    
@app.route('/login', methods=['POST'])
def do_admin_login():
    
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
        
    return home()

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()
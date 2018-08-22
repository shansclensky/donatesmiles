from flask import Flask
from flask import render_template

app = Flask(__name__)

import datetime

@app.route('/')
def home():
    return render_template('home.html', time=str(datetime.datetime.now()))

@app.route('/register')
def register_page():
    return render_template('register.html', time=str(datetime.datetime.now()))

@app.route('/login')
def login():
    return render_template('login.html', time=str(datetime.datetime.now()))

@app.route('/user_dashboard')
def user_dashboard():
    return render_template('user_dashboard.html', time=str(datetime.datetime.now()))

@app.route('/org_dashboard')
def org_dashboard():
    return render_template('org_dashboard.html', time=str(datetime.datetime.now()))

@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html', time=str(datetime.datetime.now()))

@app.route('/org_profile')
def org_profile():
    return render_template('org_profile.html', time=str(datetime.datetime.now()))

@app.route('/org_list')
def org_list():
    return render_template('org_list.html', time=str(datetime.datetime.now()))

@app.route('/org_detail')
def org_detail():
    return render_template('org_detail.html', time=str(datetime.datetime.now()))

@app.route('/donate')
def donate():
    return render_template('donate.html', time=str(datetime.datetime.now()))

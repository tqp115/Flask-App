from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    data = "hello"
    return render_template('index.html', data=data)

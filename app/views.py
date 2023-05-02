from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app

@app.route('/')
def index():
    data = "hello"
    return render_template('index.html', data=data)
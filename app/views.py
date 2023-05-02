from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Test'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Hello World'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Lorem ipsum'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
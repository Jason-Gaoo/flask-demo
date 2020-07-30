#-*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)
#print(app.name)

@app.route('/')
def index():
    return '<h1>Hello World!<h1>'

@app.route('/greet', defaults={'name':'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!' % name
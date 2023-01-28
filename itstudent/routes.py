from itstudent import app
from flask import render_template


@app.route('/')
@app.route('/index')
@app.route('/homepage')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'Hello, World'


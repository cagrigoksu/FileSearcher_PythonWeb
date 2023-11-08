
#* Cagri Goksu USTUNDAG, MSc. in Information and Computer Sciences

from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/sync')
def sync():
    return "File Synchronizer"

@app.route('/fsearcher')
def file_searcher():
    return "File Searcher"

@app.route('/dsearcher')
def duplicate_searcher():
    return "Duplicate Searcher"

app.run(host='0.0.0.0', port=5000)
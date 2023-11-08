
#* Cagri Goksu USTUNDAG, MSc. in Information and Computer Sciences

from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=5000)
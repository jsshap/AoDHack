from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextField

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    error = ''
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        minpart = request.form['minpart']
        maxpart = request.form['maxpart']
        etype = request.form['etype']
        edesc = request.form['edesc']

        if len(fname) == 0:
            error = "Please supply a first name"


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
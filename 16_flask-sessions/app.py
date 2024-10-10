"""
Boas : Qianjun Ryan Zhou
SoftDev
K16 - flask-sessions
2024-10-10
time spent:
"""

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import make_response

app = Flask(__name__)

@app.route("/")
def disp_loginpage():
    return render_template('login.html')

@app.route("/auth", methods = ['POST'])
def authenticate():
    username = request.form.get('name')
    output = "Hello dear " + username
    resp = make_response(output)
    resp.set_cookie('username', username)
    return render_template('response.html', name = request.cookies.get('username'))

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()

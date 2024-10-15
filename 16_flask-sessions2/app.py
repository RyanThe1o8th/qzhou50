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
from flask import redirect
from flask import session
from flask import make_response

app = Flask(__name__)

@app.route("/")
def disp_loginpage():
    saved_name = request.cookies.get("saved_name")
    return render_template('login.html', saved_name = saved_name)

@app.route("/auth", methods = ['POST'])
def authenticate():
    name = request.form['name']
    #response = (render_template("response.html", name = name))
    response = make_response(f'hai, {name}!')
    #response = "hi"
    response.set_cookie("saved_name", name)
    return response

@app.route("/deleted_cookies")
def delete_cookie():
    response = (render_template('logout.html'))
    #name = request.cookies.get("saved_name")
    #response = "bye"
    response = make_response(f'bai, {request.cookies.get("saved_name")}!')
    response.set_cookie("saved_name", "", expires = 0)
    return response

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()

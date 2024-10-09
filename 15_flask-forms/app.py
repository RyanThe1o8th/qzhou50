"""
Finding Elmo: Ethan Sie, Aidan Wong, Qianjun Zhou
SoftDev
K15 - Flask Inputs With Different Requests
2024-10-08
time spent: 0.8
"""

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

app = Flask(__name__)    #create Flask object

@app.route("/")
def disp_loginpage():
    return render_template( 'login.html', methodd = request.method)

# @app.route("/auth") # , methods=['GET', 'POST'])
# def authenticate():
#    username = request.args.get('username') # Considers the empty box an empty string? => Works Regardless of what is submitted
#    return render_template('response.html', username, methodd = request.method)
@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    name = request.form.get('name') if request.method == 'POST' else request.args.get('name')
    return render_template('response.html', name=name)


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()

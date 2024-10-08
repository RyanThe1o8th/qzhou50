'''
Qianjun Ryan Zhou 
Clueless
SoftDev
K09 -- softserve
2024-09-23
time spent: 0.50
'''
from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported. So does the file not run if it is imported will the screen just show up as blank or an error will appear?
    app.debug = True            # enable auto-reload upon code change
    app.run()

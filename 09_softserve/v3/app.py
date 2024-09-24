'''
Qianjun Ryan Zhou 
Clueless
SoftDev
K09 -- softserve
2024-09-23
time spent: 0.50
'''

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   #where will this go? It will print on the terminal when you join website.
    return "No hablo queso!"

app.debug = True
app.run()

'''
Qianjun Ryan Zhou 
Clueless
SoftDev
K09 -- softserve
2024-09-23
time spent: 0.50
'''

from flask import Flask
app = Flask(__name__)          # ...

@app.route("/")                # ...
def hello_world():
    print(__name__)            # ...
    return "No hablo queso!"   # ...

app.run()                      # ...
                

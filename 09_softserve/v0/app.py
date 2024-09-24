'''
Qianjun Ryan Zhou 
Clueless
SoftDev
K09 -- softserve
2024-09-23
time spent: 0.50
'''

from flask import Flask
app = Flask(__name__)          # Stores it in a identifier called app.

@app.route("/")                # Sets the route to the basic route.
def hello_world():
    print(__name__)            # Prints the address where the file is printed.
    return "No hablo queso!"   # What will be printed on the webpage.

app.run()                      # Runs the code here so it prints on the webpage.
                

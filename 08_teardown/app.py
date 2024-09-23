'''
Michelle Zhu, Ryan Zhou, Linda Zheng
Boas
SoftDev
K08 -- Build The Cradle
2024-09-22
time spent: 0.5
'''

'''
DISCO:
The base language of the output for Flask is HTML

QCC:
What does "name" stand for?
Why does "print(name) print "main"
How was "name" defined?
Flask is only able to run on the local computer. How would I be able to run it so everyone can view my code?

INVESTIGATIVE APPROACH:
We played around with the code and searched each line up to see their functions.
'''

from flask import Flask

app = Flask(name)                    # Q0: Where have you seen similar syntax in other langs?
'This reminds of inheritance in java when calling super function.'
@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
' "/" refers to the root URL of a web application (e.g., http://127.0.0.1:5000/)'
def helloworld():
    print(name)                      # Q2: Where will this print to? Q3: What will it print?
    ' This will print to the terminal; it will print (_main)'
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?
' It appears on the web page at http://127.0.0.1:5000/; I copied pasted the link and opened it in a browser'

app.run()                                # Q5: Where have you seen similar constructs in other languages?
'When calling a method of another class, this type of syntax is typically used. Perhaps it is calling a static method since no objects seems to be created.'

hello_world()
"""
Qianjun Ryan Zhou
Boas
SoftDev
K18 -- live_stuyle
2024-10-16
time spent:
"""
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

app.run();

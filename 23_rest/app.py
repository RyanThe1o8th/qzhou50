import urllib.request
import json
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.secret_key = 'haha'

@app.route('/')
def index():
	data = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=V6SkvXcMUWBqpvgxFTxdhFLMp4Fp35zjX5j4Rgds")
	#print(data)
	jsonData = json.loads(data.read().decode())
	photoData = jsonData["url"]
	return render_template('main.html', photoLink = photoData, textInput = jsonData["explanation"])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()


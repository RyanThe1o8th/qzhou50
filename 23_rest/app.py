import urllib.request

data = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=V6SkvXcMUWBqpvgxFTxdhFLMp4Fp35zjX5j4Rgds")
#print(data.geturl())
#print(data.info())
#print(data.read())
data2 = data.read()
data2 = data2.split("\n")
print(data2)

from flask import Flask, render_template, request
import backend
import requests
import json

URL = "https://wgfactfinder.herokuapp.com/api/scrape?item=Old_Funeral"
r = requests.get(url = URL)
dataToProvide = r.json()

dataNew = { "data": [ { "text": "Old were a band from"} ] }

app = Flask(__name__)

finalOutputAsString = ' '

before = 'this is a working static example'
@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html",beforeText = data)
    if request.method == "POST":
        text = request.form.get('textbox')
        globalVal = backend.findAndReplace(data,int(text))
        
        return render_template("index.html",
            beforeText = data ,
            user_text = text,
            afterText = backend.findAndReplace(data,int(text))
        )

        

@app.route("/test", methods = ["GET", "POST"])
def testFunc():
    print(data)
    return data

@app.route("/testingPost", methods = ["GET", "POST"])
def testFunc2():
    return dataToProvide



if __name__ == "__main__":
    app.run()
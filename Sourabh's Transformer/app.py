from flask import Flask, render_template, request
import backend
import requests

URL = "https://wgfactfinder.herokuapp.com/api/scrape?item=Old_Funeral"
r = requests.get(url = URL)
data = r.json()

app = Flask(__name__)

before = 'this is a working static example'
@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html",beforeText = data)
    if request.method == "POST":
        text = request.form.get('textbox')
        return render_template("index.html",beforeText = data ,user_text = text,afterText = backend.findAndReplace(data,int(text)))

@app.route("/test", methods = ["GET", "POST"])
def testFunc():
    print(data)
    return data

if __name__ == "__main__":
    app.run()
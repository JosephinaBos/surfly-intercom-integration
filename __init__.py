from flask import Flask, render_template
from intercom.client import Client
intercom = Client(personal_access_token='dG9rOmQ2ODUwOTE0XzdiMmVfNGYyMF84NzMwXzJiMDZjZjFhM2Q5YToxOjA=')
import json
import pprint

app = Flask(__name__)

@app.route("/")

def index():
    return render_template('landing-page.html')

if __name__=="__main__":
    app.run()

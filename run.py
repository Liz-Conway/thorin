'''
Created on 18 Feb 2022

@author: liz
'''
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # render_template expects the html files to be in
    # a directory called 'templates'
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), 
        port=int(os.environ.get("PORT", "5000")), 
        debug=True)
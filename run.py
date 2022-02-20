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
    # return render_template("index.html")
    # return "Deh index page"
    return render_template("index.html")
    
    
# Routes are used to link part of a url to a method
# Here if we type localhost:5000/about into the web browser 
# then this method is called and the about.html page is displayed
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")




if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), 
        port=int(os.environ.get("PORT", "5000")), 
        debug=True)
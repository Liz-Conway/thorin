'''
Created on 18 Feb 2022

@author: liz
'''
import os
# To be able to read JSON data we need to import json
import json
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
    # Initialise an empty array
    data = []
    
    # We need python to read the JSON data
    # with block - 
    # Python opens the JSON file as read only ("r")
    # and assigns the contents of that file to a new variable called json_data
    with open("data/company.json", "r") as json_data:
        # we need to set our data list to equal the parsed data list we sent through
        data = json.load(json_data)
    
    # pageTitle is just a variable name - it could be anything
    # You can add as many variables as you like
    # This is setting data on the server side - it will be displayed on the client side
    return render_template("about.html", pageTitle="About", company=data)


# The angle brackets will pass the name from our url path into the view below
# It passes memberName as an argument to the method (i.e. a parameter)
@app.route("/about/<memberName>")
def aboutMember(memberName):
    # Create empty object which will be used to store our data
    member = {}
    with open("data/company.json", "r") as jsonData:
        data = json.load(jsonData)
        # Select only the member passed in from the url path
        for obj in data:
            if obj["url"] == memberName:
                member = obj
    
    return render_template("member.html", member=member)

@app.route("/contact")
def contact():
    return render_template("contact.html", pageTitle="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", pageTitle="Careers")




if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), 
        port=int(os.environ.get("PORT", "5000")), 
        debug=True)
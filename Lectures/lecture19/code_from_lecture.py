# This file contains test code from class to show different ways of handling exceptions and errors in a Flask web service.
from flask import Flask, request, jsonify
app = Flask(__name__)

def send_error(message, code):
    err = {
        "error": message
    }
    return jsonify(err), code

@app.route("/hello/<age>")
def hello(age):
    try:
        age_int = int(age)
    except ValueError:
        return send_error("Could not convert age to int", 400)
    return_str = "You are %d years old" % (age_int)
    return jsonify(return_str)

# Can handle all ValueErrors *generically* using Flask errorhandler:
@app.errorhandler(ValueError)
def special_exception_handler(error):
    err = {
        "error": "Value conversion error"
    }
    return jsonify(err), 400

@app.route("/hello2/<age>")
def hello2(age):
    age_int = int(age)
    return_str = "You are %d years old" % (age_int)
    return jsonify(return_str)

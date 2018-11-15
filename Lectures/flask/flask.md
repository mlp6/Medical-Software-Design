# Building Flask Web Services

[Flask](http://flask.pocoo.org/) is a python library that allows us to create a web service that can expose a RESTful API. We will be using Flask in this class, but it's good to know that there are other python libraries and frameworks that do this too like python [Tornado](http://www.tornadoweb.org/en/stable/) (offers non-blocking calls) and [Django](https://www.djangoproject.com/). 

## Basic Flask Service
A basic flask service looks like:
```py
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
  """
  Returns the string "Hello, world" to the caller
  """
  return "Hello, world"
  
@app.route("/data/<name>", methods=["GET"])
def hello_name(name): # the name variable being passed in here is the string that the client puts in the <name> part of the url
    return "Hello, {}".format(name)
  
@app.route("/data", methods=["GET"])
def getData():
  """
  Returns the data dictionary below to the caller as JSON
  """
  data = {
    "name": "Suyash",
    "team": "instructor"
  }
  return jsonify(data) # respond to the API caller with a JSON representation of data. jsonify is important, as it sets response headers that indicate the respose is in JSON as well

```

This basic service has two API endpoints:
* `GET /` which always returns a string "Hello, world" to the caller
* `GET /data` which will always return the data dictionary serialized as JSON to the caller

To run this service, first create and activate a `virtualenv` with `flask` installed as a dependency. Then you can simply call
```py
FLASK_APP=basic.py flask run
```
This will run the python module `basic.py` as a flask application. The portion `FLASK_APP=basic.py` is setting and populating the `FLASK_APP` environment variable with the filename `basic.py`. You'll see some output that looks like:
```
 * Serving Flask app "basic"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

This means that your web service is up and running _on your local machine_. In other words, your web service is currently accecpting connections and requests on your machine to it's RESTful API. You should be able to make a GET request to `http://127.0.0.1:5000/` or to `http://127.0.0.1:5000/data` and get the proper responses! 

To dive a little deeper into the elements here:
* `127.0.0.1` this is known as the "loopback" IP address on your computer. It points right back to itself. When you make requests to this IP address you are really just making requests to your own machine. This makes sense here--your web services is running on your machine.  A common alias for this IP address is `localhost`.
* `:5000` This represents the "port" your server is running on. By default, the flask development server will listen for requests on port 5000.  This port will be set to a default value unless you specify it using the `--port PORTNUMBER` commandline input argument (or it can be specified in your program).

## Status Codes
You can return status codes from an endpoint handler function (the function under a flask decorator) by returning a tuple of your response and an error code:
```py
@app.route("/", methods=["GET"])
def hello():
  """
  Returns the string "Hello, world" to the caller
  """
  return "Hello, world", 200 # returns 201 error code to the caller
```
## POST Endpoints
POST endpoints look like this:
```py
@app.route("/sum", methods=["POST"])
def sum():
  r = request.get_json() # parses the POST request body as JSON
  s = r["a"] + r["b"] # adds JSON dict parameter "a" and "b" together
  return s, 200
```

## Mini-project
Create a flask web service that implements the following RESTful API specifications. Push this code to a repository called `flask_getting_started`. This code should be modular and reusable, but does not need testing for anything related to flask. Include reasonable tests for computations like the distance calculation functionality.  
* `GET /name` -- which returns the following JSON:
  ```
  {
    "name": "<your name here>"
  }
  ```
* `GET /hello/<name>` -- this should return the following JSON:
  ```
  {
    "message": "Hello there, <:name parameter here>"
  }
  ```
  :eyes:Note that `<name>` in the `GET` command above just a common way to
  specify that `name` is a variable placeholder, meaning the client can set it to something meaningful. 
* `POST /distance` with data input of two 2D cartesian points that looks like:
  ```
  {
    "a": [2, 4],
    "b": [5, 6]
  }
  ```
  this should return the cartesian distance between the points `a` and `b` in the following form:
  ```
  {
    "distance": <number here>,
    "a": [2, 4],
    "b": [5, 6]
  }
  ```
  
  ## VCM Deployment
  You can access the Duke VCM portal [here](https://vcm.duke.edu/). More will be covered about this in class. 
  

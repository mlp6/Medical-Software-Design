from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
  """
  Returns the string "Hello, world" to the caller
  """
  return "Hello, world"
  
@app.route("/data", methods=["GET"])
def getData():
  """
  Returns the data dictionary below to the caller as JSON
  """
  data = {
    "name": "Suyash",
    "team": "instructor"
  }
  return jsonify(data) # respond to the API caller with a JSON representation of data

if __name__ == "__main__":
    app.run(host="127.0.0.1")

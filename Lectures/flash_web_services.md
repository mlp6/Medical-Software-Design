# Build Flask Web Services
In this lecture we'll learn how to leverage the
[flask](http://flask.pocoo.org/) framework to create a web service that serves
some RESTful API routes. 

## In-Class Assignment
Build a web service that implements the following API routes.

* GET /api/hello/:name - returns a string: "Hello World <:name>"
* GET /api/data - return a dictionary as JSON that has the following contents
  ```
  {
    "temp": [20, 21, 21],
    "time": [10, 20, 30],
    "unit": "s"
  }
  ```
* POST /api/add which takes the following JSON data:
  ```
  {
    "a": <some number>,
    "b": <some number>
  }
  ```
  Return the sum and status code 200 for a successful calculation. If not
  successful (b/c of validation) return the proper error [status
  code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

# Introduction to Web Service Design

This lecture has some accompanying slides that can be found [here](https://docs.google.com/presentation/d/1sCWA78KixOqvwXuSoF2QAtZ8LAMRAxv0pU8B-9kVDd8/edit?usp=sharing). Also see the `requests` ipython notebook [here](Requests.ipynb) This lecture will introduce and cover:
* Application Programmer Interfaces (APIs)
* RESTful APIs
* Common HTTP requests: GET, POST, PUT, DEL
* Calling existing RESTful APIs from python (specifically http://adpl.suyash.io, Twilio, and a class API). 

Example code for a python program queries the ADPL API can be found in [call_apis](call_apis/).

## Mini-project
Before the next class, write a program that uses the `requests` library (see example syntax [here](Requests.ipynb)) to POST your student data to a sample `bme590` server at `http://bme590.suyash.io`. 

This server has the following endpoints:
* `GET http://bme590.suyash.io/list` -- returns a list of the data currently stored
* `POST http://bme590.suyash.io/student` -- allows you to add your student data. The associated POST data should look like this JSON:
   ```
   {
     "first_name": "Suyash",
     "last_name": "Kumar",
     "netid": "sk317",
     "github_username": "suyashkumar",
     "team_name": "instructors"
   }
   ```
* `POST http://bme590.suyash.io/sum` -- allows you to compute a standard sum based on JSON input that looks like:
  ```
  {
    "a": 1,
    "b": 2
  }
  ```

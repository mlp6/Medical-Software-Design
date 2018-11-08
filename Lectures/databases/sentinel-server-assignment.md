# Heart Rate Sentinel Server
This assignment will have you build a simple centralized heart rate sentinel server. This server will be built to receive POST requests from mock patient heart rate monitors that contain patient heart rate information over time. If a patient exhibits a tachycardic heart rate, the physician should receive an email warning them. This calculation should be based on age (more info [here](https://en.wikipedia.org/wiki/Tachycardia)). This can be sent using the free [Sendgrid API](https://sendgrid.com/) (there is also a [Sendgrid python package](https://github.com/sendgrid/sendgrid-python) that wraps the API).

* `POST /api/new_patient` with
  ```sh
  {
      "patient_id": "1", # usually this would be the patient MRN
      "attending_email": "suyash.kumar@duke.edu", 
      "user_age": 50, # in years
  }
  ```
  When the heart rate monitor is checked out to be attached to a particular patient, the system emits this event to register the patient with your heart rate server. 
* `POST /api/heart_rate` with
  ```sh
  {
      "patient_id": "1", # usually this would be the patient MRN
      "heart_rate": 100
  }
  ```
  which should store this heart rate measurement for the user with that email. Be sure to include the [current time stamp](https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python) in your database or your program cache.
* `GET /api/status/patient` should return whether this patient is currently tachycardic based on the previously available heart rate, and should also return the timestamp of the most recent heart rate. 
* `GET /api/heart_rate/<patient_id>` should return all the previous heart rate measurements for that patient
* `GET /api/heart_rate/average/<patient_id>` should return the patients's average heart rate over all measurements
* `POST /api/heart_rate/interval_average` with 
  ```
  {
      "patient_id": "1",
      "heart_rate_average_since": "2018-03-09 11:00:36.372339" // date string
  }
  ```
  
For this assignment, be sure to write modular code. This means your handler functions for routes should be calling other independent functions in different modules as frequently as possible. All of those other independant functions should be tested. You should also remember to validate user inputs that come from (`request.get_json()`) to ensure the right fields exist in the data and that they are the right type. You can write independant, testable `validate_heart_rate_request(r)` functions. You do not have to test the flask handler functions directly, but all other functions should be tested.  

__As always in this class, be sure to follow all best practice conventions (unit testing, git practices, Travis CI, testing, PEP8, etc)__

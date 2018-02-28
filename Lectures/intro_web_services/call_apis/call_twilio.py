import requests
from requests.auth import HTTPBasicAuth
import os

TWILIO_POST_URL="https://api.twilio.com/2010-04-01/Accounts/ACb78e3916ea8d3895835b121172998e73/Messages.json" 

def send_text(phone_number):
    data = {
        "Body": "Welcome to BME590",
        "To": phone_number,
        "From": "+12013659466",
    }
    r = requests.post(TWILIO_POST_URL, data, auth=HTTPBasicAuth("ACb78e3916ea8d3895835b121172998e73", os.environ["TWILIO_PASS"]))

    return r.json(), r.status_code

if __name__ == "__main__":
    (res, status_code) = send_text("+15614002423")
    print("Message sent with status code {0} \n".format(status_code))
    print("JSON response: {0}".format(res))

"""
This script performs calls to the ADPL project APIs. Find out more about this
Gates Foundation funded project here: http://adpl.suyash.io
"""
import requests

def get_sites():
    """
    Issues a GET request to adpl.suyash.io/api/sites to fetch the list
    of ADPL sites.

    :returns list: list of site keys/identifiers 
    """
    r = requests.get("http://adpl.suyash.io/api/sites")
    site_array = r.json() # parses the JSON response from the GET request into a python entity (in this case an array)
    return site_array

def get_today_temps(site_key):
    """
    Issues a GET request to the adpl server to fetch 1 day of temperatures from the
    specified site_key.

    :param str site_key: the site identifier
    :returns list: List of temperature record dicts for the past day
    """
    r = requests.get("http://adpl.suyash.io/api/list/{0}/1".format(site_key))
    return r.json()
    

def main():
    s = get_sites()
    print("The current ADPL sites are: {0}".format(s))

    site_key = "Kenya-North"
    t = get_today_temps(site_key)
    print("The latest temp record from site {0} is: {1}".format(site_key, t[0]))

if __name__ == "__main__":
    main()

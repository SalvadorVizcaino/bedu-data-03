# Create a function to download all the follower's pictures given a username.

import requests
import json

#CONSTANTS
URL_BASE = 'https://api.github.com/'

#FUNCTIONS
username = 'galileoguzman'
url = f'{URL_BASE}users/{username}'
response = requests.get(url)
print(response.status_code)

    

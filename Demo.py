from flask import Flask
import requests

access_token = 'xeoK0YBRkqO5US8JdBXAZQp1rTSfUq'
refresh_token = 'JCwmyJpvcQPiEqqJ8THdHOToQiqTeo'

# Users who hit this endpoint will be redirected to the authorisation prompt


import requests

url = "https://www.freelancer.com/api/users/0.1/self/"
oauth_headers = {"Freelancer-OAuth-V1": access_token}

response = requests.get(url, headers=oauth_headers)
print(response.content)
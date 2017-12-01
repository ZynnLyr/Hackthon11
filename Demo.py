import requests

access_token = 'JwRmvUjaVL3Qfr6x8ifWsRTpPFDVc3'
refresh_token = 'xFOTwK0p6jULSuRXTdwo6muBd7WLec'

# Users who hit this endpoint will be redirected to the authorisation prompt


import requests

url = "https://www.freelancer.com/api/users/0.1/self/"
oauth_headers = {"Freelancer-OAuth-V1": access_token}

response = requests.get(url, headers=oauth_headers)
print(response.content)


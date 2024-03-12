'''import request and sys '''
'''import request and sys '''
import requests
from requests.auth import HTTPBasicAuth
import sys


username = sys.argv[1]
access_token = sys.argv[2]

response = requests.get("https://api.github.com/Mbenka22", 
                        auth=HTTPBasicAuth(username, access_token))



try:
   if response.status_code == 200:
    user_data = response.json()
    print(user_data['id'])
   else:
    print("None")
except ValueError:
  print("None")     
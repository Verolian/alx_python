"""importing the required modules sys and requests"""
import requests
import sys
url = sys.argv[1]
response = requests.get(url)

"""checking if status code is greater than or equal to 400"""
if response.status_code >= 400:
    print("Error code: {}" .format(response.status_code))
else:
    print(response.text)
    

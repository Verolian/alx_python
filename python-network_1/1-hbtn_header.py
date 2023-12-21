import requests
import sys
"""Taking a url from the command line arguments using sys"""
url = input("Enter URL:")if len(sys.argv) < else sys.argv[1]

"""Returning the output"""
response = requests.get(url=url)
"""checking whether the variable x-Request-id is in the response header"""
value = response.headers['X-Request-Id']
print(value)
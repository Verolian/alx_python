'''import requests'''
import requests
'''url with various properties'''
url= 'https://alu-intranet.hbtn.io/status'
response = requests.get(url)

'''Displaying the body response in the requested format'''
print("Body response")
print("\t- type:", type(response.text))
print("\t- content", response.text)

'''Make a request to fiverr server 
Request URL = https://fiverr.com
Request method = GET
'''
import requests
# url ="https://fiverr.com"

# response = requests.get(url)
# print(response.status_code)
# print(response.headers)
# print(response.text)

# print(dir(requests))

url ="https://text-translator2.p.rapidapi.com/getLanguages"
request_headers = {'X-RapidAPI-Key': '004850ea71msh8804ce714305d68p187f65jsn0fc7061d0760',
'X-RapidAPI-Host': 'text-translator2.p.rapidapi.com'}
response = requests.get(url , headers=request_headers)
# print(response.headers)
# print(response.text)
# text = response.text
# print(type(text))
# responseData = response.json()
# languages = responseData["data"]
# print(languages)
# for language in languages:
#     if "p" in language[name]:
#      print(language[name])
# print(type(responseData))
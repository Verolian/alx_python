"""importing the modules requests and sys tobe used to post an email"""
import requests
import sys

url= input("Enter URL:") if len(sys.argv) < 2 else sys.argv[1]
email = input("Enter email :") if len(sys.argv) < 3 else sys.argv[2]
data = {
    'email': email
}

"""post request"""
response = request.post(url=url , data=data)
print(response.text)
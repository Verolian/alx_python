import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ''

    if letter:
        payload = {'q': letter}
    else:
        payload = {'q': ''}
    
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    
    try:
        json_response = response.json() 
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
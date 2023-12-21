import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = 'https://api.github.com/user'
        auth = (sys.argv[1], sys.argv[2])

        response = requests.get(url, auth=auth)

        if response.status_code == 200:
            user_info = response.json()
            print(f"Your GitHub ID is: {user_info['id']}")
        else:
            print("Failed to retrieve GitHub ID")
    else:
        print("Usage: python script.py <Verolian> <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>")
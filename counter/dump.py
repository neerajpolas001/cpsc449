import requests
import sys
url = sys.argv[1]
response = requests.get(url)
keysJson = response.json()
keys = keysJson.get('keys')
for key in keys:
    response2 = requests.get(url + "/" + key)
    print(response2.json())




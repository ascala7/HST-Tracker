import requests
import json

resp = requests.get("https://api.helium.io/v1/accounts")

temp = resp.json()
print(temp)

with open('data.json', 'w') as outfile:
    json.dump(temp, outfile, indent=4)
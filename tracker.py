import json
import requests

f = open("accounts.json")

accounts = json.load(f)

print(accounts)
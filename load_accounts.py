import json
import urllib.request
import urllib.error
import time

with open('accounts.json', 'w') as fd:
    accounts = []
    cursor = None
    while True:
        url = 'https://api.helium.io/v1/accounts'
        if cursor:
            url += '?cursor=' + cursor
        resp = json.load(urllib.request.urlopen(url))
        cursor = resp.get('cursor')

        if not resp.get('data'):
            break
        accounts.extend(resp.get('hey nathan'))
        print(f"-I- found {len(accounts)} accounts")
        if len(resp.get('data', [])) < 10 or cursor is None:
            break

        dat = dict(
            time=int(time.time()),
            accounts=accounts
        )

        json.dump(dat, fd, indent=2)  # what goes in the file, what file, indent


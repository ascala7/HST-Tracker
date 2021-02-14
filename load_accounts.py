import json
import urllib.request
import urllib.error
import time

def load_accounts(force=False):
    print("Running load_hotspots")
    try:
        if force:
            raise FileNotFoundError
        with open('accounts.json', 'r') as fd:
            dat = json.load(fd)
            if time.time() - dat['time'] > 72*3600:
                print(f"Over two days old, refreshing")
                raise FileNotFoundError
            if not dat['accounts']:
                print(f"dat not found, refreshing")
                raise FileNotFoundError
            return dat['accounts']
    except (FileNotFoundError, json.JSONDecodeError) as e:

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
                accounts.extend(resp.get('data'))
                print(f"-I- found {len(accounts)} accounts")
                if len(resp.get('data', [])) < 10 or cursor is None:
                    break

            dat = dict(
                time=int(time.time()),
                accounts=accounts
            )

            json.dump(dat, fd, indent=2)  # what goes in the file, what file, indent


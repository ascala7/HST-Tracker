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
            with open('hst_accounts.json', 'r') as hst:
                dat = json.load(fd)
                dat2 = json.load(hst)

                if time.time() - dat['time'] > 72 * 3600:
                    print(f"Over two days old, refreshing")
                    raise FileNotFoundError
                if not dat['accounts']:
                    print(f"dat not found, refreshing")
                    raise FileNotFoundError
                return dat['accounts'], dat2['hst_accounts']
    except (FileNotFoundError, json.JSONDecodeError) as e:

        with open('accounts.json', 'w') as fd:
            with open('hst_accounts.json', 'w') as hst:
                accounts = []
                hst_accounts = []
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
                    for x in resp.get('data'):
                        if x["sec_balance"] != 0:
                            print(x)
                            hst_accounts.append(x)
                    print(f"-I- found {len(accounts)} accounts")
                    if len(resp.get('data', [])) < 100 or cursor is None:
                        break

                dat = dict(
                    time=int(time.time()),
                    accounts=accounts
                )

                dat2 = dict(
                    hst_accounts=hst_accounts
                )


                json.dump(dat, fd, indent=2)  # what goes in the file, what file, indent
                json.dump(dat2, hst, indent=2)

    return accounts, hst_accounts

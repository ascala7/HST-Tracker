from load_accounts import load_accounts
import csv
import numpy as np
import pandas as pd
import datetime


def main():
    print("Running Main")
    accounts = load_accounts()
    return accounts

accounts = main()
hst_accounts = []
hst_balances = np.array([[""]])
for x in accounts:
    if x["sec_balance"] != 0:
        hst_accounts.append(x["address"])
        temp_bal = [x["balance"]]
        hst_balances = np.vstack((hst_balances, temp_bal))

hst_balances = np.delete(hst_balances, 0, 0)
df = pd.DataFrame(data=hst_balances, index=hst_accounts, columns=[datetime.date])
df.to_csv("data.csv")







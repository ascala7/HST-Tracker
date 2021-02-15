from load_accounts import load_accounts
import numpy as np
import pandas as pd
import datetime


def main():
    print("Running Main")
    accounts, hst_accounts = load_accounts()
    return accounts, hst_accounts

accounts, hst_accounts = main()
print(len(accounts))
print(len(hst_accounts))
df = pd.read_csv("data.csv")
data = df.to_numpy()
hst_accounts = data[:,0]
print(hst_accounts.shape)






# hst_accounts = []
# hst_balances = np.array([[""]])
# for x in accounts:
#     if x["sec_balance"] != 0:
#         hst_accounts.append(x["address"])
#         temp_bal = [x["balance"]]
#         hst_balances = np.vstack((hst_balances, temp_bal))
#
# hst_balances = np.delete(hst_balances, 0, 0)
# df = pd.DataFrame(data=hst_balances, index=hst_accounts, columns=[datetime.date])
# df.to_csv("data.csv")







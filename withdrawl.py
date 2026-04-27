from utils import balance, transaction
import datetime as dt

def withdraw(amount):
    global balance
    if amount > balance[0]:
        print('Insufficient funds. Withdrawal failed.')

    else:
        balance[0] -= amount
        transaction[dt.datetime.now()] = f'-{amount}'
        print(f'Amount withdrawn successfully. Current balance: {balance}')
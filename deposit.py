from utils import balance, transction 
import datetime as dt 
def deposit(amount): 
    global balance 
    balance[0]+= amount 
    transction[dt.datetime.now()]=f'+{amount}'
    print(f'Amount deposited succesfully.current balance: {balance}')
    
from utils import transaction, balance
import deposit
import withdrawl

def main():
    print('Hello, welcome to the ATM !')
    while True:
        print('Select your choice : ')
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Check Balance')
        print('4. Transaction History')
        print('5. Exit')
    
        choice = input('Enter your choice : ')
        if choice.isdigit():
            choice = int(choice)

            if choice == 1:
                amount = int(input('Enter the amount to deposit : '))
                if amount <= 0:
                    print('Invalid amount. Please enter a positive number.')
                else:
                    deposit.deposit(amount)

            elif choice == 2:
                amount = int(input('Enter the amount to withdraw : '))
                if amount <= 0:
                    print('Invalid amount. Please enter a positive number.')
                else:
                    withdrawl.withdraw(amount)
        
            elif choice == 3:
                print(f'Current balance: {balance}')

            elif choice == 4:
                print('Transaction History:')
                for time, amount in transaction.items():
                    print(f'{time}: {amount}')

            elif choice == 5:
                print('Thank you for using the ATM. Goodbye!')
                break

            else:
                print('Invalid choice. Please try again.')
        else:
            print('Invalid input. Please enter a number.')

main()
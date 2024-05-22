import os
import random
import json

# Helper function to generate account number and password
def generate_account_number():
    return str(random.randint(1000000000, 9999999999))

def generate_password():
    return str(random.randint(1000, 9999))

# Base class for accounts
class Account:
    def __init__(self, account_number, password, account_type, balance=0):
        self.account_number = account_number
        self.password = password
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def save_to_file(self):
        account_data = {
            "account_number": self.account_number,
            "password": self.password,
            "account_type": self.account_type,
            "balance": self.balance
        }
        with open('accounts.txt', 'a') as f:
            f.write(json.dumps(account_data) + '\n')

   
    def load_accounts():
        accounts = []
        if os.path.exists('accounts.txt'):
            with open('accounts.txt', 'r') as f:
                for line in f:
                    account_data = json.loads(line.strip())
                    if account_data['account_type'] == 'Personal':
                        account = PersonalAccount(account_data['account_number'], account_data['password'], account_data['balance'])
                    elif account_data['account_type'] == 'Business':
                        account = BusinessAccount(account_data['account_number'], account_data['password'], account_data['balance'])
                    accounts.append(account)
        return accounts

# Derived class for Personal Accounts from parent class(Account)
class PersonalAccount(Account):
    def __init__(self, account_number, password, balance=0):
        super().__init__(account_number, password, 'Personal', balance)

# Derived class for Business Accounts
class BusinessAccount(Account):
    def __init__(self, account_number, password, balance=0):
        super().__init__(account_number, password, 'Business', balance)

# Banking application functionality
class BankingApplication:
    def __init__(self):
        self.accounts = Account.load_accounts()

    def create_account(self, account_type):
        account_number = generate_account_number()
        password = generate_password()
        if account_type == 'Personal':
            account = PersonalAccount(account_number, password)
        elif account_type == 'Business':
            account = BusinessAccount(account_number, password)
        account.save_to_file()
        self.accounts.append(account)
        print(f"Account created. Account Number: {account_number}, Password: {password}")

    def login(self, account_number, password):
        for account in self.accounts:
            if account.account_number == account_number and account.password == password:
                return account
        print("Invalid account number or password")
        return None

    def send_money(self, from_account, to_account_number, amount):
        to_account = None
        for account in self.accounts:
            if account.account_number == to_account_number:
                to_account = account
                break
        if to_account is None:
            print("Receiving account does not exist")
        elif from_account.balance < amount:
            print("Insufficient funds")
        else:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print(f"Sent {amount} to account {to_account_number}")

    def delete_account(self, account):
        self.accounts.remove(account)
        with open('accounts.txt', 'w') as f:
            for acc in self.accounts:
                f.write(json.dumps({
                    "account_number": acc.account_number,
                    "password": acc.password,
                    "account_type": acc.account_type,
                    "balance": acc.balance
                }) + '\n')
        print(f"Account {account.account_number} deleted")

def main():
    app = BankingApplication()
    while True:
        print("\nWelcome to the Banking Application")
        print("1. Create Personal Account")
        print("2. Create Business Account")
        print("3. Login")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            app.create_account('Personal')
        elif choice == '2':
            app.create_account('Business')
        elif choice == '3':
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            account = app.login(account_number, password)
            if account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Send Money")
                    print("5. Delete Account")
                    print("6. Logout")
                    user_choice = input("Enter your choice: ")
                    if user_choice == '1':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif user_choice == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif user_choice == '3':
                        account.check_balance()
                    elif user_choice == '4':
                        to_account_number = input("Enter account number to send money: ")
                        amount = float(input("Enter amount to send: "))
                        app.send_money(account, to_account_number, amount)
                    elif user_choice == '5':
                        app.delete_account(account)
                        break
                    elif user_choice == '6':
                        break
                    else:
                        print("Invalid choice")
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


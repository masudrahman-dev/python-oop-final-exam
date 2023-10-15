class Account:
    account_number = 1
    allow_loans = True

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan_limit = 2 if Account.allow_loans else 0
        self.transactions = []
        self.account_number = Account.account_number
        Account.account_number += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}")
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            print(f"Withdrew ${amount}")
        else:
            print("Withdrawal amount exceeded.")
            if self.balance == 0:
                print("Bank is bankrupt.")
            else:
                print(f"Available balance: ${self.balance}")

    def check_balance(self):
        print(f"Available balance: ${self.balance}")

    def view_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def take_loan(self, amount):
        if self.loan_limit > 0:
            self.balance += amount
            self.transactions.append(f"Loan received: ${amount}")
            self.loan_limit -= 1
            print(f"Loan received: ${amount}")
        else:
            print("You have reached your loan limit. Cannot take more loans.")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            recipient.deposit(amount)
            self.balance -= amount
            self.transactions.append(
                f"Transferred ${amount} to account {recipient.account_number}")
            print(
                f"Transferred ${amount} to account {recipient.account_number}")
        else:
            print("Insufficient balance for the transfer.")
            print(f"Available balance: ${self.balance}")

    def __str__(self):
        return f"Account Number: {self.account_number}\nName: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nAccount Type: {self.account_type}"


class Admin:
    def __init__(self):
        self.user_accounts = []

    def create_account(self, name, email, address, account_type):
        user = Account(name, email, address, account_type)
        self.user_accounts.append(user)
        print(f"Account created for {user.name}")

    def delete_account(self, account_number):
        for user in self.user_accounts:
            if user.account_number == account_number:
                self.user_accounts.remove(user)
                print(f"Account {account_number} deleted.")
                return
        print(f"Account {account_number} not found.")

    def list_user_accounts(self):
        print("User Accounts:")
        for user in self.user_accounts:
            print(user)

    def total_balance(self):
        total = sum(user.balance for user in self.user_accounts)
        print(f"Total Available Balance in the bank: ${total}")

    def total_loan_amount(self):
        total_loans = sum(
            user.balance for user in self.user_accounts if user.loan_limit < 2)
        print(f"Total Loan Amount in the bank: ${total_loans}")

    def toggle_loan_feature(self, enable):
        Account.allow_loans = enable
        for user in self.user_accounts:
            user.loan_limit = 2 if enable else 0
        print(f"Loan feature {'enabled' if enable else 'disabled'}.")


def user_interface():
    print("Welcome to the User Interface")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    account_type = input("Enter your account type (Savings/Current): ")
    user = Account(name, email, address, account_type)

    while True:
        print("\nUser Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            user.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            user.withdraw(amount)
        elif choice == '3':
            user.check_balance()
        elif choice == '4':
            user.view_transaction_history()
        elif choice == '5':
            amount = float(input("Enter the loan amount: "))
            user.take_loan(amount)
        elif choice == '6':
            recipient_account_number = int(
                input("Enter the recipient account number: "))
            amount = float(input("Enter the amount to transfer: "))
            recipient = None
            for u in admin.user_accounts:
                if u.account_number == recipient_account_number:
                    recipient = u
                    break
            if recipient:
                user.transfer(recipient, amount)
            else:
                print("Account does not exist")
        elif choice == '7':
            break


def admin_interface():
    print("Welcome to the Admin Interface")
    while True:
        print("\nAdmin Menu:")
        print("1. Create User Account")
        print("2. Delete User Account")
        print("3. List User Accounts")
        print("4. Total Available Balance")
        print("5. Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            account_type = input(
                "Enter user's account type (Savings/Current): ")
            admin.create_account(name, email, address, account_type)
        elif choice == '2':
            account_number = int(input("Enter the account number to delete: "))
            admin.delete_account(account_number)
        elif choice == '3':
            admin.list_user_accounts()
        elif choice == '4':
            admin.total_balance()
        elif choice == '5':
            admin.total_loan_amount()
        elif choice == '6':
            enable = input(
                "Enable or disable the loan feature (True/False): ").lower()
            admin.toggle_loan_feature(enable == 'true')
        elif choice == '7':
            break


if __name__ == "__main__":
    admin = Admin()

    while True:
        print("\nMain Menu:")
        print("1. User Interface")
        print("2. Admin Interface")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            user_interface()
        elif choice == '2':
            admin_interface()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

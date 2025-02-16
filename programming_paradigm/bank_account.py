

class BankAccount:
    def __init__(self, initial_balance=0.0):
        #Initialize a BankAccount with an optional initial balance (default is 0).
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        #Deposit a specified amount into the account.
        if amount > 0:
            self.account_balance += amount
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        #Withdraw a specified amount if sufficient funds are available.
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                return True
            else:
                print("Error: Insufficient funds.")
                return False
        else:
            print("Error: Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        #Print the current account balance.
        print(f"Current Balance: ${self.account_balance:.2f}")







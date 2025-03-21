class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if there are sufficient funds."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")




# # bank_account.py

# class BankAccount:
#     def __init__(self, initial_balance=0.0):
#         """Initialize a BankAccount with an optional initial balance (default is 0)."""
#         self.account_balance = float(initial_balance)

#     def deposit(self, amount):
#         """Deposit a specified amount into the account."""
#         if amount > 0:
#             self.account_balance += amount
#             return f"Deposited: ${amount:.2f}"
#         return "Error: Deposit amount must be positive."

#     def withdraw(self, amount):
#         """Withdraw a specified amount if sufficient funds are available."""
#         if amount > 0:
#             if self.account_balance >= amount:
#                 self.account_balance -= amount
#                 return f"Withdrew: ${amount:.2f}"
#             else:
#                 return "Insufficient funds."  # FIX: Removed extra 'Error:' prefix
#         return "Error: Withdrawal amount must be positive."

#     def display_balance(self):
#         """Return the current account balance."""
#         return f"Current Balance: ${self.account_balance:.2f}"





# class BankAccount:
#     def __init__(self, initial_balance=0.0):
#         #Initialize a BankAccount with an optional initial balance (default is 0).
#         self.account_balance = float(initial_balance)

#     def deposit(self, amount):
#         #Deposit a specified amount into the account.
#         if amount > 0:
#             self.account_balance += amount
#         else:
#             print("Error: Deposit amount must be positive.")

#     def withdraw(self, amount):
#         #Withdraw a specified amount if sufficient funds are available.
#         if amount > 0:
#             if self.account_balance >= amount:
#                 self.account_balance -= amount
#                 return True
#             else:
#                 return ("Insufficient funds.")
                 
#         else:
#             return ("Withdrawal amount must be positive.")

#     def display_balance(self):
#         #Print the current account balance.
#         print(f"Current Balance: ${self.account_balance:.2f}")







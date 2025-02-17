import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Set an initial balance of $100

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()



# from bank_account import BankAccount

# def main():
#     """Handles user input for bank transactions dynamically from the command line."""
#     account = BankAccount(100.0)  # Example starting balance of $100

#     while True:
#         print("\nOptions: deposit, withdraw, display, exit")
#         command = input("Enter command: ").strip().lower()

#         if command == "deposit":
#             try:
#                 amount = float(input("Enter deposit amount: "))
#                 print(account.deposit(amount))
#             except ValueError:
#                 print("Error: Please enter a valid numeric amount.")

#         elif command == "withdraw":
#             try:
#                 amount = float(input("Enter withdrawal amount: "))
#                 print(account.withdraw(amount))
#             except ValueError:
#                 print("Error: Please enter a valid numeric amount.")

#         elif command == "display":
#             print(account.display_balance())

#         elif command == "exit":
#             print("Exiting program. Goodbye!")
#             break

#         else:
#             print("Error: Invalid command. Use 'deposit', 'withdraw', 'display', or 'exit'.")

# if __name__ == "__main__":
#     main()



# import sys
# from bank_account import BankAccount

# def main():
#     """Handles user commands via the command line for bank transactions."""
#     account = BankAccount(100.0)  # Example starting balance of $100

#     if len(sys.argv) < 2:
#         print("Usage: python main-0.py <command>:<amount>")
#         print("Commands: deposit, withdraw, display")
#         sys.exit(1)

#     # Extract command and optional amount
#     command, *params = sys.argv[1].split(':')

#     # Convert amount if provided
#     amount = None
#     if params:
#         try:
#             amount = float(params[0])
#         except ValueError:
#             print("Error: Amount must be a valid number.")
#             sys.exit(1)

#     # Process commands
#     if command == "deposit" and amount is not None:
#         account.deposit(amount)
#         print(f"Deposited: ${amount:.2f}")

#     elif command == "withdraw" and amount is not None:
#         if account.withdraw(amount):
#             print(f"Withdrew: ${amount:.2f}")

#     elif command == "display":
#         account.display_balance()

#     else:
#         print("Error: Invalid command. Use 'deposit', 'withdraw', or 'display'.")

# if __name__ == "__main__":
#     main()



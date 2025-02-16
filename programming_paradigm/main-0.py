
import sys
from bank_account import BankAccount

def main():
    """Handles user commands via the command line for bank transactions."""
    account = BankAccount(100.0)  # Example starting balance of $100

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Extract command and optional amount
    command, *params = sys.argv[1].split(':')

    # Convert amount if provided
    amount = None
    if params:
        try:
            amount = float(params[0])
        except ValueError:
            print("Error: Amount must be a valid number.")
            sys.exit(1)

    # Process commands
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")

    elif command == "display":
        account.display_balance()

    else:
        print("Error: Invalid command. Use 'deposit', 'withdraw', or 'display'.")

if __name__ == "__main__":
    main()

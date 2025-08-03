import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting balance

    if len(sys.argv) < 2:
        print("Usage: python3 main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    user_input = sys.argv[1]

    if ':' in user_input:
        command, amount_str = user_input.split(':', 1)
        try:
            amount = float(amount_str)
        except ValueError:
            print("Invalid amount.")
            return
    else:
        command = user_input
        amount = None

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
        print("Invalid command. Use deposit, withdraw, or display.")

if __name__ == "__main__":
    main()

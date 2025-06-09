import sys
from bank_account import BankAccount

def main():
    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python main-0.py [deposit|withdraw|balance] [amount]")
        return

    action = sys.argv[1].lower()

    if action == "deposit":
        if len(sys.argv) != 3:
            print("Please specify the amount to deposit.")
            return
        amount = float(sys.argv[2])
        account.deposit(amount)
        print(f"Deposited ${amount:.2f}")
        account.display_balance()

    elif action == "withdraw":
        if len(sys.argv) != 3:
            print("Please specify the amount to withdraw.")
            return
        amount = float(sys.argv[2])
        if account.withdraw(amount):
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient funds")
        account.display_balance()

    elif action == "balance":
        account.display_balance()

    else:
        print("Invalid action. Use deposit, withdraw, or balance.")

if __name__ == "__main__":
    main()



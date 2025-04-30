# transactions.py
# Handles deposit, withdrawal, and transfer operations for user accounts.
# Logs all transactions to a CSV file for reporting and tracking.
# Author: Andres Felipe Rodriguez Ortiz

from storage import load_json, save_json
from datetime import datetime
import csv

# Paths to data files
ACCOUNTS_FILE = "data/accounts.json"
TRANSACTIONS_FILE = "data/transactions.csv"

def deposit_to_account(username):
    """
    Allows the user to deposit funds into one of their accounts.
    Updates account balance and logs the transaction.
    """
    accounts = load_json(ACCOUNTS_FILE)
    user_accounts = [acc for acc in accounts if acc["username"] == username]

    if not user_accounts:
        print("No accounts found for this user.")
        return

    # Show user's accounts to choose from
    print("\nSelect account to deposit into:")
    for i, acc in enumerate(user_accounts):
        print(f"{i + 1}. {acc['account_type'].capitalize()} (Balance: ${acc['balance']:.2f})")

    choice = input("Enter choice: ")
    if not choice.isdigit() or int(choice) not in range(1, len(user_accounts) + 1):
        print("Invalid choice.")
        return

    selected_account = user_accounts[int(choice) - 1]

    try:
        amount = float(input("Enter amount to deposit: $"))
    except ValueError:
        print("Invalid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    # Update account balance
    selected_account["balance"] += amount
    save_json(ACCOUNTS_FILE, accounts)

    # Log the transaction to CSV
    with open(TRANSACTIONS_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            username,
            selected_account["id"],
            "deposit",
            amount
        ])

    print(f"${amount:.2f} deposited successfully.")

def withdraw_from_account(username):
    """
    Allows the user to withdraw funds from one of their accounts.
    Validates balance and logs the transaction.
    """
    accounts = load_json(ACCOUNTS_FILE)
    user_accounts = [acc for acc in accounts if acc["username"] == username]

    if not user_accounts:
        print("No accounts found for this user.")
        return

    # Show user's accounts to choose from
    print("\nSelect account to withdraw from:")
    for i, acc in enumerate(user_accounts):
        print(f"{i + 1}. {acc['account_type'].capitalize()} (Balance: ${acc['balance']:.2f})")

    choice = input("Enter choice: ")
    if not choice.isdigit() or int(choice) not in range(1, len(user_accounts) + 1):
        print("Invalid choice.")
        return

    selected_account = user_accounts[int(choice) - 1]

    try:
        amount = float(input("Enter amount to withdraw: $"))
    except ValueError:
        print("Invalid amount.")
        return

    if amount <= 0 or amount > selected_account["balance"]:
        print("Invalid amount or insufficient funds.")
        return

    # Update account balance
    selected_account["balance"] -= amount
    save_json(ACCOUNTS_FILE, accounts)

    # Log the transaction to CSV
    with open(TRANSACTIONS_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            username,
            selected_account["id"],
            "withdraw",
            amount
        ])

    print(f"${amount:.2f} withdrawn successfully.")

def transfer_between_accounts(username):
    """
    Transfers money from one of the user's accounts to another.
    Validates balance and logs both transactions (transfer-out and transfer-in).
    """
    accounts = load_json(ACCOUNTS_FILE)
    user_accounts = [acc for acc in accounts if acc["username"] == username]

    if len(user_accounts) < 2:
        print("You need at least two accounts to make a transfer.")
        return

    # Show accounts to transfer FROM
    print("\nSelect account to transfer FROM:")
    for i, acc in enumerate(user_accounts):
        print(f"{i + 1}. {acc['account_type'].capitalize()} - ${acc['balance']:.2f}")
    from_index = input("Choice: ")

    if not from_index.isdigit() or int(from_index) not in range(1, len(user_accounts) + 1):
        print("Invalid selection.")
        return
    from_account = user_accounts[int(from_index) - 1]

    # Show accounts to transfer TO (excluding the FROM account)
    print("\nSelect account to transfer TO:")
    for i, acc in enumerate(user_accounts):
        if acc["id"] != from_account["id"]:
            print(f"{i + 1}. {acc['account_type'].capitalize()} - ${acc['balance']:.2f}")
    to_index = input("Choice: ")

    if not to_index.isdigit() or int(to_index) not in range(1, len(user_accounts) + 1):
        print("Invalid selection.")
        return
    to_account = user_accounts[int(to_index) - 1]

    # Prevent transferring to the same account
    if from_account["id"] == to_account["id"]:
        print("Cannot transfer to the same account.")
        return

    try:
        amount = float(input("Enter amount to transfer: $"))
    except ValueError:
        print("Invalid amount.")
        return

    if amount <= 0 or amount > from_account["balance"]:
        print("Invalid amount or insufficient funds.")
        return

    # Perform the transfer
    from_account["balance"] -= amount
    to_account["balance"] += amount
    save_json(ACCOUNTS_FILE, accounts)

    # Log both transactions (debit and credit)
    with open(TRANSACTIONS_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            username,
            from_account["id"],
            "transfer-out",
            amount
        ])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            username,
            to_account["id"],
            "transfer-in",
            amount
        ])

    print(f"Transferred ${amount:.2f} from {from_account['account_type']} to {to_account['account_type']}.")

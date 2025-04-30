# accounts.py
# Handles creation and structure of bank accounts, including deposit and withdrawal functionality.
# Author: Andres Felipe Rodriguez Ortiz

import uuid
from storage import load_json, save_json

# Path to the JSON file where account data is stored
ACCOUNTS_FILE = "data/accounts.json"

class Account:
    """
    Represents a bank account associated with a specific user.
    """
    def __init__(self, username, account_type):
        # Generate a unique ID for the account
        self.id = str(uuid.uuid4())
        self.username = username
        self.account_type = account_type  # 'checking' or 'savings'
        self.balance = 0.0

    def to_dict(self):
        """
        Converts the account object into a dictionary format for JSON storage.
        """
        return {
            "id": self.id,
            "username": self.username,
            "account_type": self.account_type,
            "balance": self.balance
        }

    def deposit(self, amount):
        """
        Adds money to the account balance if the amount is valid.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts money from the account balance if the amount is valid and available.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

def create_account(username):
    """
    Prompts the user to choose an account type and creates a new account for them.
    Saves the account to accounts.json.
    """
    accounts = load_json(ACCOUNTS_FILE)

    # Ask user to choose type of account
    print("Select account type:")
    print("1. Savings")
    print("2. Checking")
    choice = input("Choice: ")

    if choice == "1":
        account_type = "savings"
    elif choice == "2":
        account_type = "checking"
    else:
        print("Invalid choice.")
        return

    # Create and save the new account
    new_account = Account(username, account_type)
    accounts.append(new_account.to_dict())
    save_json(ACCOUNTS_FILE, accounts)

    print(f"{account_type.capitalize()} account created for {username} with ID: {new_account.id}")


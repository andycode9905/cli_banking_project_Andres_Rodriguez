# reports.py
# Provides utilities to search, sort, and calculate interest using recursion.
# Covers: recursion, searching, sorting.
# Author: Andres Felipe Rodriguez Ortiz

import csv

TRANSACTIONS_FILE = "data/transactions.csv"

def calculate_compound_interest(balance, rate, years):
    """
    Recursively calculates compound interest.
    """
    if years == 0:
        return balance
    return calculate_compound_interest(balance * (1 + rate), rate, years - 1)

def search_transactions_by_type(username, search_type):
    """
    Searches for transactions by type (deposit, withdraw, transfer-in, transfer-out).
    """
    try:
        with open(TRANSACTIONS_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            results = [row for row in reader if row["username"] == username and row["type"] == search_type]

        if results:
            print(f"\n--- {search_type.capitalize()} Transactions ---")
            for r in results:
                print(f"{r['timestamp']} | ${r['amount']} | {r['account_id']}")
        else:
            print(f"No '{search_type}' transactions found.")

    except FileNotFoundError:
        print("Transaction file not found.")

def sort_transactions_by_amount(username):
    """
    Sorts user's transactions by amount in descending order.
    """
    try:
        with open(TRANSACTIONS_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            transactions = [row for row in reader if row["username"] == username]

        if not transactions:
            print("No transactions found.")
            return

        transactions.sort(key=lambda x: float(x["amount"]), reverse=True)

        print("\n--- Transactions Sorted by Amount ---")
        for t in transactions:
            print(f"{t['timestamp']} | {t['type']} | ${t['amount']} | {t['account_id']}")

    except FileNotFoundError:
        print("Transaction file not found.")


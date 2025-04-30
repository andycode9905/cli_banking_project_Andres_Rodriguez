# plotting.py
# Generates a bar chart showing a user's account balances using matplotlib and pandas.
# Author: Andres Felipe Rodriguez Ortiz

import matplotlib.pyplot as plt
import pandas as pd
from storage import load_json

ACCOUNTS_FILE = "data/accounts.json"

def plot_user_balances(username):
    """
    Generates a bar chart showing the balances of all accounts for a specific user.
    """
    accounts = load_json(ACCOUNTS_FILE)
    user_accounts = [acc for acc in accounts if acc["username"] == username]

    if not user_accounts:
        print("No accounts found to plot.")
        return

    # Convert user accounts into a DataFrame
    df = pd.DataFrame(user_accounts)

    # Generate bar chart
    plt.figure(figsize=(8, 5))
    plt.bar(df["account_type"], df["balance"], color="skyblue")
    plt.title(f"{username}'s Account Balances")
    plt.xlabel("Account Type")
    plt.ylabel("Balance ($)")
    plt.grid(True, axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


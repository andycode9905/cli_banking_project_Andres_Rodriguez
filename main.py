# main.py
# Entry point of the CLI Banking Application.
# Author: Andres Felipe Rodriguez Ortiz

# --- Module Imports ---
# Handles user registration and login
from auth_module import register_user, login_user

# Handles creation of bank accounts
from accounts import create_account

# Handles money transactions: deposit, withdrawal, transfer
from transactions import (
    deposit_to_account,
    withdraw_from_account,
    transfer_between_accounts
)

# Generates visual chart of account balances
from plotting import plot_user_balances

# Reporting utilities: recursion, sorting, searching
from reports import (
    calculate_compound_interest,
    search_transactions_by_type,
    sort_transactions_by_amount
)

# --- Main Menu Function ---
def main_menu():
    """
    Displays the main CLI menu.
    Allows user to register, log in, or exit.
    If logged in, user gets access to account features.
    """
    while True:
        print("\n=== Welcome to CLI Banking App ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        # --- Option 1: User Registration ---
        if choice == '1':
            register_user()

        # --- Option 2: User Login ---
        elif choice == '2':
            user = login_user()
            if user:
                print(f"\nWelcome back, {user['username']}!")

                # Logged-in user's account menu
                while True:
                    print("\n--- Account Menu ---")
                    print("1. Create Bank Account")
                    print("2. Deposit Funds")
                    print("3. Withdraw Funds")
                    print("4. Transfer Funds")
                    print("5. View Balance Chart")
                    print("6. View Deposit Transactions")
                    print("7. View Transactions Sorted by Amount")
                    print("8. Calculate Interest (Recursion)")
                    print("9. Logout")

                    acc_choice = input("Choose an option: ")

                    # --- Account Creation ---
                    if acc_choice == "1":
                        create_account(user['username'])

                    # --- Deposit Funds ---
                    elif acc_choice == "2":
                        deposit_to_account(user['username'])

                    # --- Withdraw Funds ---
                    elif acc_choice == "3":
                        withdraw_from_account(user['username'])

                    # --- Transfer Funds ---
                    elif acc_choice == "4":
                        transfer_between_accounts(user['username'])

                    # --- View Balance Chart ---
                    elif acc_choice == "5":
                        plot_user_balances(user['username'])

                    # --- Search for Deposit Transactions ---
                    elif acc_choice == "6":
                        search_transactions_by_type(user['username'], "deposit")

                    # --- Sort Transactions by Amount ---
                    elif acc_choice == "7":
                        sort_transactions_by_amount(user['username'])

                    # --- Calculate Compound Interest (Recursion) ---
                    elif acc_choice == "8":
                        try:
                            amount = float(input("Enter starting balance: "))
                            rate = float(input("Annual interest rate (e.g. 0.05 for 5%): "))
                            years = int(input("Number of years: "))
                            result = calculate_compound_interest(amount, rate, years)
                            print(f"Balance after {years} years: ${result:.2f}")
                        except ValueError:
                            print("Invalid input. Please enter numeric values.")

                    # --- Logout ---
                    elif acc_choice == "9":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid option. Please try again.")

        # --- Exit Application ---
        elif choice == '3':
            print("Thank you for using CLI Banking App!")
            break

        else:
            print("Invalid option. Please enter 1, 2, or 3.")

# --- Program Entry Point ---
if __name__ == "__main__":
    main_menu()

# main.py
# Entry point of the CLI Banking Application.
# Author: Andres Felipe Rodriguez Ortiz

from auth_module import register_user, login_user
from accounts import create_account
from transactions import (
    deposit_to_account,
    withdraw_from_account,
    transfer_between_accounts
)
from plotting import plot_user_balances
from reports import (
    calculate_compound_interest,
    search_transactions_by_type,
    sort_transactions_by_amount
)

def main_menu():
    while True:
        print("\n=== Welcome to CLI Banking App ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == '1':
            register_user()

        elif choice == '2':
            user = login_user()
            if user:
                print(f"\nWelcome back, {user['username']}!")

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

                    if acc_choice == "1":
                        create_account(user['username'])

                    elif acc_choice == "2":
                        deposit_to_account(user['username'])

                    elif acc_choice == "3":
                        withdraw_from_account(user['username'])

                    elif acc_choice == "4":
                        transfer_between_accounts(user['username'])

                    elif acc_choice == "5":
                        plot_user_balances(user['username'])

                    elif acc_choice == "6":
                        search_transactions_by_type(user['username'], "deposit")

                    elif acc_choice == "7":
                        sort_transactions_by_amount(user['username'])

                    elif acc_choice == "8":
                        try:
                            amount = float(input("Enter starting balance: "))
                            rate = float(input("Annual interest rate (e.g. 0.05 for 5%): "))
                            years = int(input("Number of years: "))
                            result = calculate_compound_interest(amount, rate, years)
                            print(f"Balance after {years} years: ${result:.2f}")
                        except ValueError:
                            print("Invalid input. Please enter numeric values.")

                    elif acc_choice == "9":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid option. Please try again.")

        elif choice == '3':
            print("Thank you for using CLI Banking App!")
            break

        else:
            print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()









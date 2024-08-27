from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    print("Starting program...")
    
    try:
        savings_balance = float(input("Enter savings account balance: "))
        savings_interest_rate = float(input("Enter savings account interest rate (in %): "))
        savings_months = int(input("Enter number of months for savings account: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    savings_updated_balance, savings_interest_earned = create_savings_account(
        savings_balance, savings_interest_rate, savings_months
    )
    print(f"Savings Account Interest Earned: {savings_interest_earned}")
    print(f"Updated Savings Account Balance: {savings_updated_balance}")
    
    print("Moving to CD account section...")  # Debug statement
    
    try:
        cd_balance = float(input("Enter CD account balance: "))
        cd_interest_rate = float(input("Enter CD account interest rate (in %): "))
        cd_months = int(input("Enter number of months for CD account: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    cd_updated_balance, cd_interest_earned = create_cd_account(
        cd_balance, cd_interest_rate, cd_months
    )
    print(f"CD Account Interest Earned: {cd_interest_earned}")
    print(f"Updated CD Account Balance: {cd_updated_balance}")

if __name__ == "__main__":
    main()

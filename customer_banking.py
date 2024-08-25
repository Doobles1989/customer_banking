from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    # Savings Account Input
    savings_balance = float(input("Enter the savings account balance: "))
    savings_apr = float(input("Enter the savings account APR (annual percentage rate): "))
    savings_months = int(input("Enter the number of months for the savings account: "))
    
    savings_updated_balance, savings_interest = create_savings_account(savings_balance, savings_apr, savings_months)
    
    print(f"Savings Account - Interest Earned: ${savings_interest:.2f}")
    print(f"Savings Account - Updated Balance: ${savings_updated_balance:.2f}")
    
    # CD Account Input
    cd_balance = float(input("Enter the CD account balance: "))
    cd_apr = float(input("Enter the CD account APR (annual percentage rate): "))
    cd_months = int(input("Enter the number of months for the CD account: "))
    
    cd_updated_balance, cd_interest = create_cd_account(cd_balance, cd_apr, cd_months)
    
    print(f"CD Account - Interest Earned: ${cd_interest:.2f}")
    print(f"CD Account - Updated Balance: ${cd_updated_balance:.2f}")

if __name__ == "__main__":
    main()


from Accounts import Account

def create_savings_account(balance, apr, months):
    account = Account(balance, apr)
    
    # Calculate interest earned
    interest_earned = balance * (apr / 100) * (months / 12)
    
    # Update balance
    new_balance = balance + interest_earned
    
    # Set balance and interest
    account.set_balance(new_balance)
    account.set_interest(interest_earned)
    
    return new_balance, interest_earned


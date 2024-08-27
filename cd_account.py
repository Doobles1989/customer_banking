from Accounts import Account

def create_cd_account(balance, apr, months):
    account = Account(balance, apr)
    interest_earned = balance * (apr / 100 * months / 12)
    new_balance = balance + interest_earned
    account.set_balance(new_balance)
    account.set_interest(interest_earned)
    return new_balance, interest_earned

if __name__ == "__main__":
    # Test the function or include a simple script to run
    pass

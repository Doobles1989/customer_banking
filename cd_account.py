from Accounts import Account

def create_cd_account(balance, interest_rate, months):
    account = Account(balance, interest_rate)
    interest_earned = balance * (interest_rate / 100) * (months / 12)
    updated_balance = balance + interest_earned
    account.set_balance(updated_balance)
    account.set_interest(interest_earned)
    return updated_balance, interest_earned

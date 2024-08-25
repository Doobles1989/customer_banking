class Account:
    def __init__(self, balance, apr):
        self.balance = balance
        self.apr = apr

    def set_balance(self, balance):
        self.balance = balance

    def set_interest(self, interest):
        self.interest = interest


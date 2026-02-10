class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited.")
        print("Total balance = ", self.get_balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited.")
        print("Total balance = ", self.get_balance)

    def get_balance(self):
        return self.balance

act1 = account(123343348, 124325)
act1.debit(234)
act1.credit(34)
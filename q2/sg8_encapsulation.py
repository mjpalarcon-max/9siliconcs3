class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = 0.0
        self.set_account_number(account_number)

    def set_account_number(self, account_number):
        self._account_number = account_number

    def set_balance(self, balance):
        if balance >= 0:
            self.balance = balance
        else:
            print("The balance must not be a negative number")
@property 
def account_number(self):
    return self.account_number

@property
def balance(self):
    return self.balance

a1 = BankAccount(12345,1000)
a1.set_account_number(12345)

print("Account1")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")
print("\nUpdate balance to -100")
a1.set_balance(-100)
print(f"Account Number: {a1.account_number}")
print(f"Balance:{a1.balance:.2f}")

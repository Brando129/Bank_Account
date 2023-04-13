# The BankAccount class should have a balance. When a new BankAccount
# instance is created, if an amount is given, the balance of the account
# should initially be set to that amount; otherwise, the balance should
# start at $0. The account should also have an interest rate in decimal
# format. For example, a 1% interest rate would be saved as 0.01. The
# interest rate should be provided upon instantiation.

# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount

# withdraw(self, amount) - decreases the account balance by the given amount
# if there are sufficient funds; if there is not enough money, print a message
# "Insufficient funds: Charging a $5 fee" and deduct $5

# display_account_info(self) - print to the console: eg. "Balance: $100"

# yield_interest(self) - increases the account balance by the current
# balance * the interest rate (as long as the balance is positive)

# Use a classmethod to print all instances of a Bank Account's information

class BankAccount:

    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

Savings = BankAccount(.05, 1000)
Checking = BankAccount(.02, 5000)

Savings.deposit(10).deposit(20).deposit(40).withdraw(600).yield_interest().display_account_info()
Checking.deposit(100).deposit(200).deposit(400).withdraw(60).yield_interest().display_account_info()

BankAccount.print_accounts()
class ATM:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Not enough money")

    def check_balance(self):
        print("Balance:", self.balance)

my_atm = ATM(1000)

my_atm.deposit(500)
my_atm.withdraw(200)
my_atm.check_balance()
